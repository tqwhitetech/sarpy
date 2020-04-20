import os
from sarpy.annotation.schema_processing import LabelSchema

schema_output_path = os.path.expanduser("~/Downloads/sample_schema.json")

version = "0.0"

labels = {"0": "terrain",
          "1": "mountain",
          "2": "field",
          "3": "structure",
          "4": "radio tower",
          "5": "building",
          "6": "skyscraper",
          "7": "house",
          "8": "water",
          "9": "lake",
          "10": "stream",
          "11": "river",
          "12": "creek"
          }

subtypes = {"0": ["1", "2"],
            "3": ["4", "5"],
            "5": ["6", "7"],
            "8": ["9", "10"],
            "10": ["11", "12"]
            }

confidence = ["0", "1", "2"]

label_schema = LabelSchema(version, labels, subtypes, confidence)

label_schema.to_file(schema_output_path)
