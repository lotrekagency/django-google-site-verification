

def test_verify_site(client):
    content = client.get('/google11a50bcc62df11b5.html').content
    assert '11a50bcc62df11b5' in str(content)
