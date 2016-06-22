from horizon_autotests.steps import generate_ids


def test_edit_image(image, images_steps):
    new_name = image.name + ' (updated)'
    images_steps.update_image(name=image.name, new_name=new_name)
    image.name = new_name


def test_delete_images(images_count, create_images):
    images_names = list(generate_ids(prefix='image', count=images_count))
    create_images(images_names)


def test_create_image_from_local_file()
