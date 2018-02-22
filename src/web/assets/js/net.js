function netMapInit(){
    var nodes = new vis.DataSet([
        {id: 1, label: 'SRX1500'},
        {id: 2, label: 'EX4600'},
        {id: 3, label: 'EX4600'},
        {id: 4, label: 'EX2200'},
        {id: 5, label: 'EX2200'}
    ]);

    // create an array with edges
    var edges = new vis.DataSet([
        {from: 1, to: 3},
        {from: 1, to: 2},
        {from: 2, to: 4},
        {from: 2, to: 5}
    ]);

    // create a network
    var container = document.getElementById('mynetwork');

    // provide the data in the vis format
    var data = {
        nodes: nodes,
        edges: edges
    };
    var options = {};

    // initialize your network!
    var network = new vis.Network(container, data, options);
}