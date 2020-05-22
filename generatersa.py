import rsa

(pub, priv) = rsa.newkeys(2048)

pubex = str(pub)
privex = str(priv)

pubfile = open("tartare_public_key.tart", "w")
pubfile.write(pubex)
pubfile.close()

privfile = open("tartare_private_key.tart", "w")
privfile.write(privex)
privfile.close()
