import base64

# 读取 imLam.txt 的内容
with open("imLam.txt", "rb") as f:
    content = f.read()

# 对内容进行 Base64 编码
encoded_content = base64.b64encode(content)

# 将编码后的内容写入 imLam.txt
with open("imLam.txt", "wb") as f:
    f.write(encoded_content)
