"""
This file is for executing everything together
"""
import filehandling as fiha
import id3algorithm as id3


filepathnames = "datasets/cardaten/carnames.txt"
filepathdata = "datasets/cardaten/car.data"

# read data
classes, attributes, attribute_values = fiha.read_data_names(filepath=filepathnames)
instances = fiha.read_data(filepath=filepathdata)
print("Number of Classes: " + str(len(classes)))
print("Number of Attributes: " + str(len(attributes)))
print("Number of Instances: " + str(len(instances)))

# at this point call the id3 algorithm and build tree
dtree = id3.builddtree(classes=classes, instances=instances, attributes=attributes,
                       attributesvalues=attribute_values, attributesleft=attributes.copy())
print("ID3 algorithm finished")

# at this point call the xml writer
fiha.write_xml(dtree=dtree)
print("XML writing finished")
# attributes: buying, maint, doors, persons, lug_boot, safety
# instance = ["high", "med", "5more", "more", "med", "high"]
# print(id3.getclass(dtree, instance, attributes))
# print("start calculating accuracy")
# print("Accuracy =" + str(id3.getaccuracy(dtree=dtree, instances=instances, attributes=attributes)))

