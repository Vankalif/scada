var chartColors = {
    red: 'rgb(255, 99, 132)',
    orange: 'rgb(255, 159, 64)',
    yellow: 'rgb(255, 205, 86)',
    green: 'rgb(75, 192, 192)',
    blue: 'rgb(54, 162, 235)',
    purple: 'rgb(153, 102, 255)',
    grey: 'rgb(201, 203, 207)'
  };


var chrtFontColor = 'rgb(218, 214, 209)';
var chrtGridColor = 'rgb(133, 139, 146)';
var chrtFontSize = 16;


var ctx = document.getElementById('tempChart').getContext('2d');
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30'],
        datasets: [{
            label: 'скважина 36',
            borderColor: chartColors.green,
            backgroundColor: chartColors.green,
            fill: false,
            data: [19, 57, 55, 69, 95, 91, 52, 87, 94, 72, 17, 55, 63, 76, 14, 59, 17, 78, 77, 59, 38, 88, 58, 46, 12, 45, 4, 68, 24, 70, 76]
        }]
    },

    // Configuration options go here
    options: {
        legend: {
            labels: {
                fontColor: chrtFontColor
            }
        },
        title: {
            display: true,
            text: 'Температура',
            fontColor: chrtFontColor,
            fontSize: chrtFontSize,
        },
        scales: {
            yAxes: [{
                gridLines: {
                    color: chrtGridColor
                },
                ticks: {
                    fontColor: chrtFontColor
                }
            }],
            xAxes: [{
                gridLines: {
                    color: chrtGridColor
                },
                ticks: {
                    fontColor: chrtFontColor
                }
            }],
        },
    }
});

var ctx = document.getElementById('levelChart').getContext('2d');
var chart = new Chart(ctx, {
    // The type of chart we want to create
    type: 'line',

    // The data for our dataset
    data: {
        labels: ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30'],
        datasets: [{
            label: 'скважина 36',
            borderColor: chartColors.green,
            backgroundColor: chartColors.green,
            fill: false,
            data: [51, 58, 9, 10, 15, 45, 15, 58, 8, 57, 10, 59, 63, 3, 27, 47, 22, 5, 52, 8, 69, 60, 27, 31, 11, 40, 56, 67, 20, 35, 48]
        }]
    },

    // Configuration options go here
    options: {
        legend: {
            labels: {
                fontColor: chrtFontColor
            }
        },
        title: {
            display: true,
            text: 'Уровень',
            fontColor: chrtFontColor,
            fontSize: chrtFontSize,
        },
        scales: {
            yAxes: [{
                gridLines: {
                    color: chrtGridColor
                },
                ticks: {
                    fontColor: chrtFontColor
                }
            }],
            xAxes: [{
                gridLines: {
                    color: chrtGridColor
                },
                ticks: {
                    fontColor: chrtFontColor
                }
            }],
        },
    }
});