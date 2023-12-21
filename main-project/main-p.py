import sys
import main_m as main
import module.module as module
import module.sub_module.sub_m as Smodule
sys.path.append("C:\\Users\\HAYAT TRADERS\\Desktop\\py")
main.name()
module.name()
Smodule.name()


print(sys.path)


import sup_m as super
super.name()