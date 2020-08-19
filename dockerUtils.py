import docker

def cleanImages():
    print("Removing all images ... ")
    client = docker.from_env()
    allImages = client.images.list(all=True)
    for i in allImages:
        try:
            client.images.remove(image=i.id, force=True)
            print("Removed : " + str(i))
        except:
            print("Failed to remove this image : " + str(i))

cleanImages()