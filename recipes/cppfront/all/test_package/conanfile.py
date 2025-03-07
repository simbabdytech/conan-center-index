from conan import ConanFile
from conan.tools.files import copy
from conan.tools.layout import basic_layout
import os


class TestPackageConan(ConanFile):
    settings = "os", "arch", "compiler", "build_type"
    generators = "VirtualRunEnv"

    def layout(self):
        basic_layout(self)

    def requirements(self):
        self.requires(self.tested_reference_str)

    def build(self):
        copy(self, "pure2-hello.cpp2", src=self.recipe_folder, dst=self.build_folder)
        self.run("cppfront {}".format(os.path.join(self.build_folder, "pure2-hello.cpp2")), env="conanrun")

    def test(self):
        self.run("cppfront -h", env="conanrun")
        assert os.path.isfile(os.path.join(self.build_folder, "pure2-hello.cpp"))
