function netMapInit(){

    // create a network
    var container = document.getElementById('mynetwork');

    if(container != null) {
        console.log(container);
        var nodes = new vis.DataSet([
            {id: 1, label: 'SRX1500', shape: 'image', image: 'assets/device.png'},
            {id: 2, label: 'EX4600', shape: 'image', image: 'assets/device.png'},
            {id: 3, label: 'EX4600', shape: 'image', image: 'assets/device.png'},
            {id: 4, label: 'EX4600', shape: 'image', image: 'assets/device.png'},
            {id: 5, label: 'EX2200', shape: 'image', image: 'assets/device.png'},
            {id: 6, label: 'EX4600', shape: 'image', image: 'assets/device.png'},
            {id: 7, label: 'EX2200', shape: 'image', image: 'assets/device.png'},
            {id: 8, label: 'EX2200', shape: 'image', image: 'assets/device.png'}
        ]);

        // create an array with edges
        var edges = new vis.DataSet([
            {from: 1, to: 3},
            {from: 1, to: 2},
            {from: 2, to: 4},
            {from: 2, to: 5},
            {from: 3, to: 6},
            {from: 3, to: 7},
            {from: 3, to: 8}
        ]);

        

        // provide the data in the vis format
        var data = {
            nodes: nodes,
            edges: edges
        };
        var options = {
            nodes: {
                shape: 'image',
                size:40
            }
        };

        // initialize the network!
        var network = new vis.Network(container, data, options);
    }   
}