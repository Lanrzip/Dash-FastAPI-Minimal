window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        handleSideMenuCollapse: (nClicks, inlineCollapsed) => {
            if (nClicks) {
                if (inlineCollapsed) {
                    return [
                        false,
                        'antd-arrow-left',
                        {
                            'position': 'absolute',
                            'zIndex': 1001,
                            'top': '32px',
                            'left': '264px',
                            'background': 'white',
                            'color': 'rgb(99, 115, 129)',
                            'padding': '4px',
                            'border': '1px dashed rgba(145, 158, 171, 0.2)'
                        },
                        {
                            'width': '280px',
                            'height': '100%',
                            'transition': 'width 0.2s',
                            'borderRight': '1px solid rgb(240, 240, 240)',
                            'paddingRight': 10,
                        }
                    ]
                }
                return [
                    true,
                    'antd-arrow-right',
                    {
                        'position': 'absolute',
                        'zIndex': 1001,
                        'top': '32px',
                        'left': '72px',
                        'background': 'white',
                        'color': 'rgb(99, 115, 129)',
                        'padding': '4px',
                        'border': '1px dashed rgba(145, 158, 171, 0.2)'
                    },
                    {
                        'width': '88px',
                        'height': '100%',
                        'transition': 'width 0.2s',
                        'borderRight': '1px solid rgb(240, 240, 240)',
                        'paddingRight': 10,
                    }
                ]
            }
            return window.dash_clientside.no_update;
        },

        renderChartCardDonutChart: (data) => {
            let targetIdx = window.dash_clientside.callback_context.inputs_list[0].id.index;
            console.log(data);
            var myChart = echarts.init(document.getElementById(JSON.stringify({"index": targetIdx,"type":"application-chart-card-donut-chart-container"})));
            var option;

            const total = data.reduce((sum, item) => sum + item.value, 0);

            option = {
              tooltip: {
                trigger: 'item'
              },
              legend: {
                top: '5%',
                left: 'center'
              },
              series: [
                {
                  name: 'Access From',
                  type: 'pie',
                  radius: ['40%', '70%'],
                  avoidLabelOverlap: false,
                  padAngle: 5,
                  itemStyle: {
                    borderRadius: 10
                  },
                  label: {
                    show: true,
                    position: 'center',
                    formatter: () => `{a|总计}\n \n \n {b|${total}}`,
                    rich: {
                      a: {
                        fontSize: 15,
                        color: '#637381'
                      },
                      b: {
                        fontSize: 30,
                        fontWeight: 'bold',
                      }
                    }
                  },
                  labelLine: {
                    show: false
                  },
                  data: data
                }
              ]
            };
            // 渲染
            myChart.setOption(option);
            window.addEventListener("resize", () => {
                myChart.resize();
            });
        },
        renderChartCardBarChart: (data) => {
          let targetIdx = window.dash_clientside.callback_context.inputs_list[0].id.index;
          var myChart = echarts.init(document.getElementById(JSON.stringify({"index": targetIdx,"type":"application-chart-card-bar-chart-container"})));
        
          var option;
          var series = data
          const stackInfo = {};
          for (let i = 0; i < series[0].data.length; ++i) {
            for (let j = 0; j < series.length; ++j) {
              const stackName = series[j].stack;
              if (!stackName) {
                continue;
              }
              if (!stackInfo[stackName]) {
                stackInfo[stackName] = {
                  stackStart: [],
                  stackEnd: []
                };
              }
              const info = stackInfo[stackName];
              const data = series[j].data[i];
              if (data && data !== '-') {
                if (info.stackStart[i] == null) {
                  info.stackStart[i] = j;
                }
                info.stackEnd[i] = j;
              }
            }
          }
          
          for (let i = 0; i < series.length; ++i) {
            const data = series[i].data;
            const info = stackInfo[series[i].stack];
            for (let j = 0; j < series[i].data.length; ++j) {
              const isEnd = info.stackEnd[j] === i;
              const topBorder = isEnd ? 20 : 0;
              const bottomBorder = 0;
              data[j] = {
                value: data[j],
                itemStyle: {
                  borderRadius: [topBorder, topBorder, bottomBorder, bottomBorder]
                }
              };
            }
          }
          option = {
            tooltip: {
              trigger: 'axis',
              axisPointer: {
                type: 'shadow'
              }
            },
            legend: {},
            grid: {
              left: '3%',
              right: '4%',
              bottom: '3%',
              containLabel: true
            },
            xAxis: [
              {
                type: 'category',
                data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
              }
            ],
            yAxis: [
              {
                type: 'value'
              }
            ],
            series: series
          };
          // 渲染
          myChart.setOption(option);
          window.addEventListener("resize", () => {
              myChart.resize();
          });
      }
    }
});