// document.querySelector('#search-form').addEventListener('submit', function(event) {
//     event.preventDefault();
//     console.log("start search");
//     // Get selected countries from form
//     var selectedCountries = [];
//     var select = document.querySelector('#countries');
//     for (var i = 0; i < select.options.length; i++) {
//         if (select.options[i].selected) {
//             selectedCountries.push(select.options[i].value);
//         }
//     }
//     console.log(selectedCountries);

//     // Send AJAX request
//     fetch('/search', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({
//             countries: selectedCountries
//         })
//     })
//     .then(function(response) {
//         return response.json();
//     })
//     .then(function(data) {
//         // Generate bar chart
//         var trace = {
//             x: data.countries,
//             y: data.unemploymentRates,
//             type: 'bar'
//         };
//         var layout = {
//             title: 'Unemployment Rates Comparison',
//             xaxis: {
//                 title: 'Country'
//             },
//             yaxis: {
//                 title: 'Unemployment Rate (%)'
//             }
//         };
        
//         Plotly.newPlot('chart', [trace], layout);
//     })
//     .catch(function(error) {
//         console.log(error);
//     });
// });

// Read the CSV file
d3.csv("unemployment_rates.csv", function(data) {

    // Define the list of available countries
    var countries = ["United States", "Mexico", "Canada"];
  
    // Define the initial set of selected countries
    var selectedCountries = ["United States"];
  
    // Filter the data to only include the selected countries
    var filteredData = data.filter(function(d) {
      return selectedCountries.indexOf(d.countries) !== -1;
    });
  
    // Define the x and y domains
    var xDomain = countries;
    var yDomain = [0, d3.max(filteredData, function(d) { return d.unemploymentRates; })];
  
    // Define the x and y scales
    var xScale = d3.scaleBand().domain(xDomain).range([0, width]).padding(0.2);
    var yScale = d3.scaleLinear().domain(yDomain).range([height, 0]);
  
    // Define the x and y axes
    var xAxis = d3.axisBottom(xScale);
    var yAxis = d3.axisLeft(yScale);
  
    // Create the chart
    var chart = d3.select("#chart")
      .append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
      .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
  
    // Add the x axis
    chart.append("g")
      .attr("class", "x-axis")
      .attr("transform", "translate(0," + height + ")")
      .call(xAxis);
  
    // Add the y axis
    chart.append("g")
      .attr("class", "y-axis")
      .call(yAxis);
  
    // Add the bars
    chart.selectAll(".bar")
      .data(filteredData)
      .enter()
      .append("rect")
      .attr("class", "bar")
      .attr("x", function(d) { return xScale(d.countries); })
      .attr("y", function(d) { return yScale(d.unemploymentRates); })
      .attr("width", xScale.bandwidth())
      .attr("height", function(d) { return height - yScale(d.unemploymentRates); });
  
    // Update the chart when the user selects new countries
    d3.selectAll(".country-checkbox").on("change", function() {
  
      // Get the list of selected countries
      selectedCountries = [];
      d3.selectAll(".country-checkbox").each(function(d) {
        if (d3.select(this).property("checked")) {
          selectedCountries.push(d);
        }
      });
  
      // Filter the data to only include the selected countries
      filteredData = data.filter(function(d) {
        return selectedCountries.indexOf(d.countries) !== -1;
      });
  
      // Update the y domain
      yDomain = [0, d3.max(filteredData, function(d) { return d.unemploymentRates; })];
  
      // Update the y scale
      yScale.domain(yDomain);
  
      // Update the y axis
      chart.select(".y-axis")
        .transition()
        .duration(1000)
        .call(yAxis);
  
      // Update the bars
      chart.selectAll(".bar")
        .data(filteredData)
        .transition()

        .duration(1000)
        .attr("y", function(d) { return yScale(d.unemploymentRates); })
        .attr("height", function(d) { return height - yScale(d.unemploymentRates); });

    });

    });