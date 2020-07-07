from powerscribe import Powerscribe

if __name__ == '__main__':
    # http://psrbtst01ta.tjh.tju.edu/RadPortal/login.aspx
    url = 'http://psrbtst01ta.tjh.tju.edu/RadPortal'
    username = "infervision"
    password = "infervision"

    accession = "12345"
    field_name = "CTRAD"
    field_value = "29997"

    with Powerscribe(url) as ps:
        if ps.sign_in(username, password):
            print("Signin successfully")
            # if ps.set_custom_field(accession, field_name, field_value):
                # print(f"Sent field name {field_name} and value {field_value} into accession {accession})
            # else:
                # print(f"Error sending field name {field_name} and value {field_value} into accession {accession}")
                
        else:
            print("Signin failed")