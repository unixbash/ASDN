class Tasks:

    __generatedConfig = []
    __hostName = ""

    def checkNetConf(self):
        commit = []
        commit.append("    - name: Checking NETCONF connectivity")
        commit.append("      wait_for:")
        commit.append('        host: "{{ ' + self.__hostName + ' }}"')
        commit.append("        port: 830")
        commit.append("        timeout: 5")

        self.__generatedConfig.append("\n".join(commit))


    def commitAndConfirm(self):
        commit = []
        #Commit the configuration
        commit.append("    - name: Merge configuration data from a file and commit")
        commit.append("      juniper_junos_config:")
        commit.append('        load: "merge"')
        commit.append('        format: "text"')
        commit.append('        src: "build_conf/{{ inventory_hostname }}/junos-config.conf"')
        commit.append('        comment: "Automated ASDN Configuration"')
        commit.append("      register: response")

        #Check commit status
        commit.append("    - name: Print the response")
        commit.append("      debug:")
        commit.append("        var: response")

        self.__generatedConfig.append("\n".join(commit))

    __taskLib = {
        "checkNetConf": checkNetConf,
        "commitAndConfirm": commitAndConfirm,
    }

    def __init__(self, providedTasks, hostName):
        self.__hostName = hostName
        #Dispatch functions which construct the taskList provided
        for task in providedTasks:
            if task in self.__taskLib:
                self.__taskLib[task](self)

    def get__generatedConfig(self):
        return self.__generatedConfig