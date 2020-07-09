# from powerscribe import Powerscribe
from powerscribe import Powerscribe

if __name__ == '__main__':
    # http://psrbtst01ta.tjh.tju.edu/RadPortal/login.aspx
    url = 'http://psrbtst01ta.tjh.tju.edu/RadPortal'
    username = "infervision"
    password = "infervision"

    # accession = "20117672"
    accession = "E00040996"
    field_name = "CTRAD"
    field_value = "29997"

    with Powerscribe(url) as ps:
        if ps.sign_in(username, password):
            print("Signin successfully")
            # Testing setting custom field
            # if ps.set_custom_field(accession, field_name, field_value):
            #     print("set succeeds")
            #     # print(f"Sent field name {field_name} and value {field_value} into accession {accession})
            # else:
            #     # print(f"Error sending field name {field_name} and value {field_value} into accession {accession}")
            #     print("set fail")
            # Testing setting custom field

            #Test getting order
            order = ps.try_get_order(accession)
            print(order)
            custom_field_defination = ps.get_custom_filed_definitions(accession)
            print(custom_field_defination)
            #Test getting order

        else:
            print("Signin failed")


    
    #Test login failed func
    # print("Testing failed log func")
    # with Powerscribe(url) as ps:
    #     if ps.sign_in("123", "123"):
    #         print("Signin successfully")
    #         if ps.set_custom_field(accession, field_name, field_value):
    #             print("set succeeds")
    #             # print(f"Sent field name {field_name} and value {field_value} into accession {accession})
    #         else:
    #             # print(f"Error sending field name {field_name} and value {field_value} into accession {accession}")
    #             print("set fail")
    #     else:
    #         print("Signin failed")