$(window).on('load',function(){
    $('#welcomeModal').modal('show');

    //Open the IKE Modal
    $('#ikeNext').click(function(){
        $('#ikeModal').modal('show');
    });

    //Open the IPsec Modal
    $('#ipsecNext').click(function(){
        $('#ipsecModal').modal('show');
    });
});