<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8"%>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>Графики</title>
    <script
            src="https://code.jquery.com/jquery-3.1.1.min.js"
            integrity="sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8="
            crossorigin="anonymous"></script>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/highcharts/5.0.9/highcharts.js"></script>
    <script>
        $(document).ready(function () {
            Highcharts.setOptions({
                global: {
                    useUTC: false
                }
            });

            Highcharts.chart('container', {
                chart: {
                    type: 'spline',
                    animation: Highcharts.svg, // don't animate in old IE
                    marginRight: 10,
                    events: {
                        load: function () {

                            // set up the updating of the chart each second
                            var series = this.series[0];
                            setInterval(function () {
                                $.ajax({
                                    url: "/data.json",
                                })
                                    .done(function (data) {
                                        var x = (new Date()).getTime();
                                        series.addPoint([x, data.d1], true, true);
                                    });
                            }, 1000);
                        }
                    }
                },
                title: {
                    text: 'Прогноз значения пропусков и ошибок платежного баланса РФ' + '\n'+' за текущий квартал'
                },
                xAxis: {
                    type: 'datetime',
                    tickPixelInterval: 150
                },
                yAxis: {
                    title: {
                        text: 'Value'
                    },
                    plotLines: [{
                        value: 0,
                        width: 1,
                        color: '#808080'
                    }]
                },
                tooltip: {
                    formatter: function () {
                        return '<b>' + this.series.name + '</b><br/>' +
                            Highcharts.dateFormat('%Y-%m-%d %H:%M:%S', this.x) + '<br/>' +
                            Highcharts.numberFormat(this.y, 2);
                    }
                },
                legend: {
                    enabled: false
                },
                exporting: {
                    enabled: false
                },
                series: [{
                    name: 'Пропуки и ошибки с учетом сомнительных операций',
                    data: (function () {
                        // generate an array of random data
                        var data = [],
                            time = (new Date()).getTime(),
                            i;

                        for (i = -19; i <= 0; i += 1) {
                            data.push({
                                x: time + i * 1000,
                                y: Math.random()
                            });
                        }
                        return data;
                    }())
                }]
            });
        });
    </script>
</head>
<body>
<div id="container"></div>
<style>
    table {
        width: 300px; /* Ширина таблицы */
        border: 5px solid #5c4980; /* Рамка вокруг таблицы */
        margin: auto; /* Выравниваем таблицу по центру окна  */
    }
    td {
        text-align: center;
    }
</style>
${title}<br/><br/>
Привет! ${user}, вашему вниманию прогнозы по сомнительным операвциям на текущий квартал.
<br/>

<table class="table">
    <tr>

        <div>
            <td><a href="/chart2">Следующий график</a></td>
        </div>
    </tr>
    <tr>
        <div>
            <td><a href="<c:url value="/logout" />">Выйти</a></td>
        </div>
    </tr>
</table>

</body>
</html>