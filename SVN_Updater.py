"""============================================================================
INFORMATION ABOUT CODE         Coding: ISO 9001:2015
===============================================================================
For Checking SVN is getting used by another process, and
if yes then it will retry the process

Author: Prajinkya Pimpalghare
Date: 12-December-2017
Version: 1.0
Input Variable: Directory Path
============================================================================"""

from __future__ import print_function
import time
import subprocess
import sys
import os


class ConflictManager(object):
    """For managing SVN conflict , when two or more SVN update is going on"""

    def __init__(self, folder_path):
        """
        Initializing the required variables
        :param folder_path:
        """
        self.folder_path = folder_path

    def svn_update(self):
        """
        This function will check continuously if SVN is locked or not
        and according to that it will react
        """
        try:
            if self.lock_checker():
                print("SVN Update Done")
            else:
                print(">", end="")
                time.sleep(5)
                self.svn_update()
        except BaseException as error:
            print("Exceeded Maximum Waiting time: "
                  "Please complete the other SVN update quickly", error)

    def lock_checker(self):
        """
        For monitoring is workspace getting updated  or not according to output of subprocess
        :return:
        """
        return subprocess.Popen("svn update " + self.folder_path, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, shell=False).stdout.read().__contains__("Updating")

    def macro(self):
        """
        For monitoring , is subprocess returning any error. If yes then it should wait
        :return:
        """
        return subprocess.Popen("svn info " + self.folder_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                shell=False).stderr.read().__contains__("not") or subprocess.Popen(
            "svn info " + self.folder_path, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            shell=False).stderr.read().__contains__("remove")

    def main(self):
        """
        It is main function , which will tigger the svn_update function according to the SVN status
        """
        if self.macro():
            print("Other Component is updating the SVN repo: Waiting")
            self.svn_update()
        else:
            print("Starting SVN Update")
            self.svn_update()


class ErrorManager(object):
    """For error handling"""

    def __init__(self, folder_path):
        """
        Initializing the required variables
        :param folder_path:
        """
        self.folder_path = folder_path

    def main(self):
        """
        It will check is directory exist or not, if exist , is it under SVN or not
        """
        if os.path.isdir(self.folder_path) or os.path.exists(self.folder_path):
            if subprocess.Popen("svn info " + self.folder_path, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, shell=False).stderr.read().__contains__("not a working copy"):
                print("Input Path is not Under SVN, Please check the path", self.folder_path)
                exit(0)
            else:
                print(self.folder_path, " is under SVN")
        else:
            print("Input path is not a proper directory, please check the path :", self.folder_path)
            exit(0)


if __name__ == '__main__':
    FOLDER_PATH = None
    try:
        FOLDER_PATH = sys.argv[1]
    except BaseException as error:
        print("Check Input argument, it is not provided correctly", error)
    ErrorManager(FOLDER_PATH).main()
    ConflictManager(folder_path=FOLDER_PATH).main()
