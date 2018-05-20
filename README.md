# ASDN - Automated Software Defined Networking

## Introduction

The project being developed is a network automation platform which will initially aid and eventually replace network engineers in configuring and making changes on a live network. This will subsequently reduce operating costs as well as the possibility of human introduced errors. The devices this platform will communicate with include, but are not limited to switches, routers and firewalls. These are not consumer, but industry grade networking appliances, ranging from thousands to hundreds of thousands of euro in value.


## Code Samples

### Below is a code snippet that generates a YAML configuration file and executes it using Ansible 
```
def generateYaml(device, commands):

    # Add to list of hosts if not present
    device.addAnsibleHost()
    #Set timestamp
    ts = time.time()
    tStamp = datetime.datetime.fromtimestamp(ts).strftime('-%H-%M-%S_%d-%m-%Y')
    path = "ansible/yaml/generated/"
    fileName = device.hostname + tStamp + ".yaml"
    fullFileName = path + fileName

    #Load templates
    env = Environment(loader = FileSystemLoader('ansible/yaml'), trim_blocks=True, lstrip_blocks=True)
    initTemplate = env.get_template('initTemplate.yaml')
    dataTemplate = env.get_template('commandTemplate.yaml')

    initData = initTemplate.render( host=device.hostname)
    commandData = "\n"

    #Generate configuration file from all given fullCommand
    no=0
    for commandLIst in commands.commands:
        for commandType, command in commandLIst.items():
            command = replaceTabsWithSpaces(command)
            commandData += dataTemplate.render( type=commandType,
                                                args=command,
                                                num=no) + "\n"
        no+=1

    finalFileData = initData + commandData

    #Execute YAML
    fileAvail =  uploadFile(finalFileData, fileName, path)
    command = "ansible-playbook " + "ansible/yaml/generated/" + fileName

    if fileAvail:
        result = callPy("2.7", "py2Exec", "executeOnServer", [command])
        if not result:
            print("Python2 script AuthenticationException")
            return False
        else:
            return str(result)
    else:
        print("Ansible Execution Failed")
        return False
```


### The below code Evaluates the Best Machine Learning Algorithm for this Application
```
#Validate the Dataset
def algoValidation(self):
    scoring = 'accuracy'
    X_train, X_validation, Y_train, Y_validation = model_selection.train_test_split(self.X, self.Y, test_size=self.size, random_state=self.seed)

    #Check the following Algorithms
    models = []
    models.append(('LR', LogisticRegression()))
    models.append(('LDA', LinearDiscriminantAnalysis()))
    models.append(('KNN', KNeighborsClassifier()))
    models.append(('CART', DecisionTreeClassifier()))
    models.append(('NB', GaussianNB()))
    models.append(('SVM', SVC()))

    #Evaluate the above algoritms
    results = []
    names = []
    for name, model in models:
        kfold = model_selection.KFold(n_splits=10, random_state=self.seed)
        cv_results = model_selection.cross_val_score(model, X_train, Y_train, cv=kfold, scoring=scoring)
        results.append(cv_results)
        names.append(name)
        msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
        print(msg)

    # Compare Algorithms
    fig = plt.figure()
    ax = fig.add_subplot(111)
    plt.boxplot(results)
    ax.set_xticklabels(names)
    plt.show()

```