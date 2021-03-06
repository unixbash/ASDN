function initCharts() {
  //Check if elements exist
  var check = document.getElementsByName("siteOne");
  var theme = ['#607d8b', '#8b6e60', '#8b8460', '#f3b49f', '#7d608b'];

  if(check.length != 0) {

    // Load the Visualization API and the corechart package.
    google.charts.load('current', {'packages':['corechart']});

    // Set a callback to run when the Google Visualization API is loaded.
    google.charts.setOnLoadCallback(siteOne);
    google.charts.setOnLoadCallback(siteTwo);
    google.charts.setOnLoadCallback(siteThree);
    google.charts.setOnLoadCallback(siteFour);

    // Device activity
    google.charts.setOnLoadCallback(deviceOne);
    google.charts.setOnLoadCallback(deviceTwo);

    

    // Callback that creates and populates a data table,
    // instantiates the pie chart, passes in the data and
    // draws it.
    function siteOne() {

      // Create the data table.
      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Data');
      data.addColumn('number', 'Percentage');
      data.addRows([
        ['Online', 1],
        ['Offline', 3],
        ['Warning', 1],
        ['Unconfigured', 2],
        ['Unsupported', 1]
      ]);

      // Set chart options
      var options = {
        'title':'HQ - Dublin Office',
        colors:theme
      };

      // Instantiate and draw our chart, passing in some options.
      var chart = new google.visualization.PieChart(document.getElementById('siteOne'));
      chart.draw(data, options);
    }

    function siteTwo() {

      // Create the data table.
      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Data');
      data.addColumn('number', 'Percentage');
      data.addRows([
        ['Online', 3],
        ['Offline', 1],
        ['Warning', 1],
        ['Unconfigured', 1],
        ['Unsupported', 2]
      ]);

      // Set chart options
      var options = {
        'title':'HQ - Cork Office',
        colors:theme
      };

      // Instantiate and draw our chart, passing in some options.
      var chart = new google.visualization.PieChart(document.getElementById('siteTwo'));
      chart.draw(data, options);
    }

    function siteThree() {

      // Create the data table.
      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Data');
      data.addColumn('number', 'Percentage');
      data.addRows([
        ['Online', 1],
        ['Offline', 1],
        ['Warning', 1],
        ['Unconfigured', 3],
        ['Unsupported', 2]
      ]);

      // Set chart options
      var options = {
        'title':'HQ - Limerick Office',
        colors:theme
      };

      // Instantiate and draw our chart, passing in some options.
      var chart = new google.visualization.PieChart(document.getElementById('siteThree'));
      chart.draw(data, options);
    }

    function siteFour() {

      // Create the data table.
      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Data');
      data.addColumn('number', 'Percentage');
      data.addRows([
        ['Online', 1],
        ['Offline', 1],
        ['Warning', 2],
        ['Unconfigured', 3],
        ['Unsupported', 1]
      ]);

      // Set chart options
      var options = {
        'title':'HQ - London Office',
        colors:theme
      };

      // Instantiate and draw our chart, passing in some options.
      var chart = new google.visualization.PieChart(document.getElementById('siteFour'));
      chart.draw(data, options);
    }

    function deviceOne() {
      var data = google.visualization.arrayToDataTable([
        ['Time', 'Dublin Office', 'Cork Office'],
        ['Jan',  100,      400],
        ['Feb',  700,      460],
        ['Mar',  800,      1120],
        ['Apr',  300,      400]
      ]);

      var options = {
        hAxis: {title: 'Month',  titleTextStyle: {color: '#333'}},
        vAxis: {title: 'Mb/s', minValue: 0}
      };

      var chart = new google.visualization.AreaChart(document.getElementById('deviceOne'));
      chart.draw(data, options);
    }

    function deviceTwo() {
      var data = google.visualization.arrayToDataTable([
        ['Time', 'Limerick Office', 'London Office'],
        ['Jan',  800,      500],
        ['Feb',  300,      1000],
        ['Mar',  1100,     300],
        ['Apr',  450,      400]
      ]);

      var options = {
        hAxis: {title: 'Month',  titleTextStyle: {color: '#333'}},
        vAxis: {title: 'Mb/s', minValue: 0}
      };

      var chart = new google.visualization.AreaChart(document.getElementById('deviceTwo'));

      chart.draw(data, options);
    }
  }

  //Check if elements exist
  var check = document.getElementsByName("routingStatuss");

  if(check.length != 0) {

    google.charts.load('current', {'packages':['corechart']});

    //Routing Status
    google.charts.setOnLoadCallback(routingStatus);

    /*Network Details*/
    function routingStatus() {
      // Create the data table.
      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Data');
      data.addColumn('number', 'Percentage');
      data.addRows([
        ['Static', 1],
        ['Direct', 1],
        ['Local', 2],
        ['Access-internal', 3]
      ]);

      var options = {
        'title':'Route Type',
        colors:theme
      };

      // Instantiate and draw our chart, passing in some options.
      var chart = new google.visualization.PieChart(document.getElementById('routingStatus'));
      chart.draw(data, options);
    }

    //VLAN and L2 Status
    google.charts.setOnLoadCallback(vlanStatus);

    function vlanStatus() {
      // Create the data table.
      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Data');
      data.addColumn('number', 'Percentage');
      data.addRows([
        ['VoIP', 1],
        ['Data', 3],
        ['CCTV', 2]
      ]);

      var options = {
        'title':'Interfaces in VLAN',
        colors:theme
      };

      // Instantiate and draw our chart, passing in some options.
      var chart = new google.visualization.PieChart(document.getElementById('vlanStatus'));
      chart.draw(data, options);
    }

    //VLAN and L2 Status
    google.charts.setOnLoadCallback(securityStatus);

    function securityStatus() {
      // Create the data table.
      var data = new google.visualization.DataTable();
      data.addColumn('string', 'Data');
      data.addColumn('number', 'Percentage');
      data.addRows([
        ['trust', 3],
        ['untrust', 1],
        ['vpn', 1]
      ]);

      var options = {
        'title':'Interfaces In Zone',
        colors:theme
      };

      // Instantiate and draw our chart, passing in some options.
      var chart = new google.visualization.PieChart(document.getElementById('securityStatus'));
      chart.draw(data, options);
    }
  }
}