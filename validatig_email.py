def fun(s):
    # return True if s is a valid email, else return False
    user_name       = s.split('@'[0])
    website_name    = (s.split('@')[1]).split('.')[0]
    extension       = (s.split('@')[1]).split('.')[1]
    
    is_valid = True
    for i in user_name:
        if i.isalpha or i.isdigit or i=="-" or i=="_":
            for j in website_name:
                if j.isalpha or j.isdigit:
                    if len(extension)==3:
                        is_valid = True
                    else:
                        is_isvalid = False
                else:
                    is_valid = False
        else:
            is_valid = False
    return is_valid

print(fun("iismailbilge@gmail.com"))
