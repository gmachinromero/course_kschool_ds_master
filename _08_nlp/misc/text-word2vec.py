#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import os
import bz2
import argparse
from nltk import word_tokenize
import logging
from gensim.models import Word2Vec


class Corpus(object):
    """Corpus class which allows to read recursively a set of directories
    containing bzip2'ed text documents (e.g. Wikipedia articles)"""

    def __init__(self, directory):
        self.directory = directory

    def __iter__(self):
        for subdir, dirs, files in os.walk(self.directory):
            for f in files:
                for line in bz2.open(os.path.join(subdir, f), "rt"):
                    line = line.lower()  # lowecase normalization
                    # avoid lines containing some XML tags between docs
                    if not line.startswith("<doc") and not line.startswith("</doc"):
                        yield word_tokenize(line)  # tokenzation


def main():
    # parse the input options
    parser = argparse.ArgumentParser(description="convert text file to vectors")
    parser.add_argument(
        "-i", "--input", action="store", dest="input", help="input directory"
    )
    parser.add_argument(
        "-n",
        "--name",
        action="store",
        dest="name",
        default="model",
        help="name of the output model",
    )
    parser.add_argument(
        "-s",
        "--size",
        action="store",
        dest="size",
        default=200,
        help="vector size (default: 200)",
    )
    parser.add_argument(
        "-w",
        "--workers",
        action="store",
        dest="workers",
        default=2,
        help="number of workers (default: 2)",
    )
    parser.add_argument(
        "-c",
        "--counts",
        action="store",
        dest="counts",
        default=10,
        help="threshold vocabulary (default: 10)",
    )
    args = parser.parse_args()

    # set the input directory
    logging.basicConfig(
        format="%(asctime)s : %(levelname)s : %(message)s", level=logging.INFO
    )
    logging.info("Processing %s" % (args.input))
    sentences = Corpus(args.input)

    logging.info(
        "Building vocabulary and training with %s workers, %s dimensions and %s minimal counts"
        % (args.workers, args.size, args.counts)
    )
    model = gensim.models.Word2Vec(
        sentences,
        min_count=int(args.counts),
        size=int(args.size),
        workers=int(args.workers),
    )
    logging.info("Saving the model in %s-%s.w2v..." % (args.name, args.size))
    model.save("./%s-%s.w2v" % (args.name, args.size))
    logging.info("Done")


if __name__ == "__main__":
    main()
