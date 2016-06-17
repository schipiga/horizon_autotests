def test_create_volume(volumes_steps):
    volumes_steps.create_volume('volume')
    volumes_steps.delete_volume('volume')
