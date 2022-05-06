def test_user_can_create_product(product):
    assert len(product.__class__.objects.all()) == 1
