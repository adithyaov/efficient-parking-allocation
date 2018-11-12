import sys
sys.path.insert(0, '3rd_party/models/tutorials/image/imagenet')
import classify_image as ci

import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
  '--model_dir',
  type=str,
  default='/tmp/imagenet',
  help=""
)
parser.add_argument(
  '--image_file',
  type=str,
  default='2.jpg',
  help='Absolute path to image file.'
)
parser.add_argument(
  '--num_top_predictions',
  type=int,
  default=5,
  help='Display this many predictions.'
)
ci.FLAGS, ci.unparsed = parser.parse_known_args()
ci.tf.app.run(main=ci.main, argv=[ci.sys.argv[0]] + ci.unparsed)