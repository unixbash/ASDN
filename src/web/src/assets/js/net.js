function netMapInit(){

    // create a network
    var container = document.getElementById('mynetwork');

    if(container != null) {
        $.get("http://localhost:8080/device/map/1", function(data, status){
            console.log(data);

            // provide the data in the vis format
            var map = {
                nodes: data.nodes,
                edges: data.edges
            };
            var options = {
                nodes: {
                    shape: 'image',
                    size:40
                }
            };

            // initialize the network!
            var network = new vis.Network(container, map, options);
            network.on( 'click', function(params) {
                console.log('clicked nodes:', params.nodes[0]);
                window.angularComponentReference.zone.run(() =>{window.angularComponentReference.componentFn(params.nodes[0]);});
            });
        });

        


    }   
}