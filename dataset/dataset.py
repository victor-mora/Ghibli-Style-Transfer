"""my_dataset dataset."""

import tensorflow_datasets as tfds


class MyDataset(tfds.core.GeneratorBasedBuilder):
  """DatasetBuilder for my_dataset dataset."""

  VERSION = tfds.core.Version('1.0.0')
  RELEASE_NOTES = {
      '1.0.0': 'Initial release.',
  }
  MANUAL_DOWNLOAD_INSTRUCTIONS = "Download data.zip"

  def _info(self) -> tfds.core.DatasetInfo:
    """Returns the dataset metadata."""
    return tfds.core.DatasetInfo(
        builder=self,
        features=tfds.features.FeaturesDict({
            # These are the features of your dataset like images, labels ...
            'image': tfds.features.Image(shape=(256, 256, 3)),
            'label': tfds.features.ClassLabel(names=['no', 'yes']),
        }),
        # If there's a common (input, target) tuple from the
        # features, specify them here. They'll be used if
        # `as_supervised=True` in `builder.as_dataset`.
        supervised_keys=('image', 'label'),  # Set to `None` to disable
    )

  def _split_generators(self, dl_manager: tfds.download.DownloadManager):
    """Returns SplitGenerators."""
    archive_path = dl_manager.manual_dir / 'data.zip'
    extracted_path = dl_manager.extract(archive_path)

    return {
        'trainA': self._generate_examples(path=extracted_path / 'data' / 'trainA'),
        'trainB': self._generate_examples(path=extracted_path / 'data' / 'trainB'),
        'testA': self._generate_examples(path=extracted_path / 'data' / 'testA'),
        'testB': self._generate_examples(path=extracted_path / 'data' / 'testB'),
    }

  def _generate_examples(self, path):
    """Yields examples."""
    for f in path.glob('*.jpg'):
      yield f.name, {
          'image': f,
          'label': 'yes' if 'Scene' in f.name else 'no',
      }

