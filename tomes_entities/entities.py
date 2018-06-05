#!/usr/bin/env python3

""" This module contain a class for converting a TOMES Excel 2007+ (.xlsx) entity dictionary
file to Stanford CoreNLP compliant text file or a JSON file. """

__NAME__ = "tomes_entities"
__DESCRIPTION__ = "Part of the TOMES project: creates a Stanford CoreNLP NER mappings file."
__URL__ = "https://github.com/StateArchivesOfNorthCarolina/tomes-entities"
__VERSION__ = "0.0.1"
__AUTHOR__ = "Nitin Arora"
__AUTHOR_EMAIL__ = "nitin.a.arora@ncdcr.gov"

# import modules.
import sys; sys.path.append("..")
import json
import logging
import logging.config
import os
import plac
import yaml
from tomes_entities.lib.xlsx_to_entities import XLSXToEntities


class Entities():
    """ A class for converting a TOMES Excel 2007+ (.xlsx) entity dictionary file to a 
    Stanford CoreNLP compliant text file or a JSON file.
    
    Example:
    >>> entities = Entities("../tests/sample_files/sampleEntityDictionary.xlsx")
    >>> #entities.entities() # generator.
    >>> entities.write_json("mappings.json")
    >>> entities.write_stanford("mappings.txt")
    """


    def __init__(self, xlsx_file):
        """ Sets instance attributes.

        Args:
            - xlsx_file (str): The path to the Excel containing a valid TOMES "Entities" 
            worksheet.
        """

        # set logging.
        self.logger = logging.getLogger(__name__)        
        self.logger.addHandler(logging.NullHandler())
        
        # set attributes.
        self.xlsx_file = xlsx_file
        
        # compose instances.
        self.x2e = XLSXToEntities()
            
    
    def entities(self):
        """ Returns a generator containing a mapped entity row (dict) for each row in 
        @self.xlsx_file.
        
        Returns:
            generator: The return value.

        Raises:
            - FileNotFoundError: If @self.xlsx_file doesn't exist.
            - KeyError: If the required "Entities" worksheet can't be retrieved.
            - self.x2e.SchemaError: If the worksheet header is invalid.
        """

        # ensure @self.xlsx_file exists.
        if not os.path.isfile(self.xlsx_file):
            msg = "Can't find file: {}".format(self.xlsx_file)
            raise FileNotFoundError(msg)
        
        # get entities from @self.xlsx_file.
        self.logger.info("Getting data from: {}".format(self.xlsx_file))
        try:
            entities = self.x2e.get_entities(self.xlsx_file)
        except Exception as err:
            err_name = type(err).__name__
            msg = ("{}: {}".format(err_name, err))
            self.logger.error(msg)
            raise Exception(msg)

        return entities


    def write_stanford(self, output_file):
        """ Converts @self.xlsx_file to a CoreNLP mapping file.
        
        Args:
            - output_file (str): The output path for the converted file.

        Returns:
            None

        Raises:
            FileExistsError: If @output_file already exists.
        """

        # ensure @output_file doesn't already exist.
        if os.path.isfile(output_file):
            err = "Destination file '{}' already exists.".format(output_file)
            self.logger.error(err)
            raise FileExistsError(err)

        # get entities.
        entities = self.entities()

        # open @output_file for writing.
        tsv = open(output_file, "w", encoding="utf-8")

        # iterate through rows; write data to @output_file.
        linebreak = False
        for entity in entities:

            # get cell data.
            tag = entity["identifier"], entity["authority"], entity["label"]
            tag = "::".join(tag)
            manifestations = entity["manifestations"]

            # write row to file and avoid final linebreak (otherwise CoreNLP will crash).
            for manifestation in manifestations:
                if linebreak:
                    tsv.write("\n")
                else:
                    linebreak = True
                tsv.write("\t".join([manifestation,tag]))
        tsv.close()

        self.logger.info("Created Stanford file: {}".format(output_file))
        return


    def write_json(self, output_file):
        """ Converts @self.xlsx_file to a JSON file.
        
        Args:
            - output_file (str): The output path for the converted file.

        Returns:
            None

        Raises:
            FileExistsError: If @output_file already exists.
        """

        # ensure @output_file doesn't already exist.
        if os.path.isfile(output_file):
            err = "Destination file '{}' already exists.".format(output_file)
            self.logger.error(err)
            raise FileExistsError(err)

        # get entities.
        entities = self.entities()

        # open @output_file for writing.
        jsv = open(output_file, "w", encoding="utf-8")
        jsv.write("[")

        # iterate through rows; write data to @output_file.
        bracket = True
        for entity in entities:
            if bracket:
                bracket = False
            else:
                jsv.write(",\n")
            jsv.write(json.dumps(entity, indent=2))
        jsv.write("]")
        jsv.close()
        
        self.logger.info("Created JSON file: {}".format(output_file))
        return


# CLI.
def main(xlsx: ".xlsx entity dictionary file", 
        output: ("output file destination"),
        JSON: ("use JSON output", "flag", "j"),
        silent: ("disable console logs", "flag", "s")):

    "Converts TOMES Entity Dictionary to Stanford CoreNLP text file or a JSON file.\
    \nexample: `py -3 entities.py ../tests/sample_files/sampleEntityDictionary.xlsx mappings.txt`"

    # make sure logging directory exists.
    logdir = "log"
    if not os.path.isdir(logdir):
        os.mkdir(logdir)

    # get absolute path to logging config file.
    config_dir = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(config_dir, "logger.yaml")
    
    # load logging config file.
    with open(config_file) as cf:
        config = yaml.safe_load(cf.read())
    if silent:
        config["handlers"]["console"]["level"] = 100
    logging.config.dictConfig(config)
    
    # create class instance.
    entities = Entities(xlsx)
    
    # set write method.
    write_func = entities.write_stanford
    if JSON:
        write_func = entities.write_json
    
    # write @output.
    logging.info("Running CLI: " + " ".join(sys.argv))
    try:
        write_func(output)
        logging.info("Done.")
        sys.exit()
    except Exception as err:
        logging.critical(err)
        sys.exit(err.__repr__())
        

if __name__ == "__main__":
    
    import plac
    plac.call(main)
