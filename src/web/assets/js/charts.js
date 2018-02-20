// Load the Visualization API and the corechart package.
google.charts.load('current', {'packages':['corechart']});

// Set a callback to run when the Google Visualization API is loaded.
google.charts.setOnLoadCallback(siteOne);
google.charts.setOnLoadCallback(siteTwo);

// Callback that creates and populates a data table,
// instantiates the pie chart, passes in the data and
// draws it.
function siteOne() {

  // Create the data table.
  var data = new google.visualization.DataTable();
  data.addColumn('string', 'Topping');
  data.addColumn('number', 'Slices');
  data.addRows([
    ['Online', 3],
    ['Offline', 1],
    ['Warning', 1],
    ['Unconfigured', 1],
    ['Unsupported', 2]
  ]);

  // Set chart options
  var options = {'title':'HQ - Dublin Office',
                 'width':400,
                 'height':300};

  // Instantiate and draw our chart, passing in some options.
  var chart = new google.visualization.PieChart(document.getElementById('siteOne'));
  chart.draw(data, options);
}

function siteTwo() {

  // Create the data table.
  var data = new google.visualization.DataTable();
  data.addColumn('string', 'Topping');
  data.addColumn('number', 'Slices');
  data.addRows([
    ['Online', 3],
    ['Offline', 1],
    ['Warning', 1],
    ['Unconfigured', 1],
    ['Unsupported', 2]
  ]);

  // Set chart options
  var options = {'title':'HQ - Dublin Office',
                 'width':400,
                 'height':300};

  // Instantiate and draw our chart, passing in some options.
  var chart = new google.visualization.PieChart(document.getElementById('siteTwo'));
  chart.draw(data, options);
}