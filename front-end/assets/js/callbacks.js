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
        },

        renderChartCardCircleChart: (data) => {
          let targetIdx = window.dash_clientside.callback_context.inputs_list[0].id.index;
          var myChart = echarts.init(document.getElementById(JSON.stringify({"index": targetIdx,"type":"e-commerce-chart-card-circle-chart-container"})));
          var option;

          option = {
            polar: {
              radius: [90, '150%']
            },
            angleAxis: {
              max: 4,
              startAngle: 90,
              axisLine: { show: false },
              axisTick: { show: false },
              axisLabel: { show: false },
              splitLine: { show: false }
            },
            radiusAxis: {
              type: 'category',
              data: data.name,
              axisLine: { show: false },
              axisTick: { show: false },
              axisLabel: { show: false },
              splitLine: { show: false }
            },
            tooltip: {
              trigger: 'item',
              formatter: function (params) {
                var totalValue = params.value;
                var label = params.name;
                var graphic = option.graphic.children[0];
                graphic.style.text = `{total|${label}}\n{value|` + totalValue/4*100 + '%' + '}';
                myChart.setOption(option);
              }
            },
            legend: {
              bottom: 10,
              data: data.name,
              textStyle: {
                color: '#333'
              }
            },
            series: [
              {
                name: data.name[0],
                type: 'bar',
                data: [data.value[0]],
                coordinateSystem: 'polar',
                itemStyle: {
                  color: '#5470c6',
                  barBorderRadius: [40, 40, 40]
                }
              },
              {
                name: data.name[1],
                type: 'bar',
                data: [data.value[1]],
                coordinateSystem: 'polar',
                itemStyle: {
                  color: '#91cc75',
                  barBorderRadius: [40, 40, 40]
                }
              },
              {
                name: data.name[2],
                type: 'bar',
                data: [data.value[2]],
                coordinateSystem: 'polar',
                itemStyle: {
                  color: '#fac858',
                  barBorderRadius: [40, 40, 40]
                }
              }
            ],
            graphic: {
              type: 'group',
              left: 'center',
              top: 'center',
              children: [
                {
                  type: 'text',
                  z: 100,
                  left: 'center',
                  top: 'middle',
                  style: {
                    fill: '#333',
                    text: `{total|Total}\n{value|${data.total}}`,
                    font: 'bolder 30px sans-serif',
                    textAlign: 'center',
                    textVerticalAlign: 'middle',
                    rich: {
                      total: {
                        fontSize: 16,
                        lineHeight: 20,
                        align: 'center'
                      },
                      value: {
                        fontSize: 24,
                        lineHeight: 30,
                        align: 'center'
                      }
                    }
                  }
                }
              ]
            }
          };
          myChart.setOption(option);
          myChart.on('mouseout', function () {
            var graphic = option.graphic.children[0];
            graphic.style.text = `{total|Total}\n{value|${data.total}}`;
            myChart.setOption(option);
          });
          window.addEventListener("resize", () => {
            myChart.resize();
          });
        },

        
        renderChartCardAreaChart: (data) => {
          let targetIdx = window.dash_clientside.callback_context.inputs_list[0].id.index;
          var myChart = echarts.init(document.getElementById(JSON.stringify({"index": targetIdx,"type":"e-commerce-chart-card-area-chart-container"})));
          var option;

          // 将十六进制颜色转换为 rgba 颜色
          function hexToRGBA(hex, alpha) {
            var r = parseInt(hex.slice(1, 3), 16);
            var g = parseInt(hex.slice(3, 5), 16);
            var b = parseInt(hex.slice(5, 7), 16);
            return 'rgba(' + r + ', ' + g + ', ' + b + ', ' + alpha + ')';
          }

          var totalExpenditure = data.y.总支出;
          var totalIncome = data.y.总收入;

          const colors = ['#00A76F', '#FFAB00'];

          // 指定图表的配置项和数据
          var option = {
              tooltip: {
                  trigger: 'axis'
              },
              legend: {
                  data: ['总收入', '总支出']
              },
              xAxis: {
                  type: 'category',
                  data: data.x
              },
              yAxis: {
                  type: 'value'
              },
              series: [
                  {
                      name: '总收入',
                      data: totalIncome,
                      type: 'line',
                      smooth: true,
                      showSymbol: false, // 不显示数据点
                      lineStyle: {
                          color: colors[0]
                      },
                      areaStyle: {
                          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                              offset: 0,
                              color: hexToRGBA(colors[0], 0.5)
                          }, {
                              offset: 1,
                              color: hexToRGBA(colors[0], 0.1)
                          }])
                      },
                      itemStyle: {
                        color: colors[0] // 设置总支出系列的图例颜色
                      }
                  },
                  {
                      name: '总支出',
                      data: totalExpenditure,
                      type: 'line',
                      smooth: true,
                      showSymbol: false, // 不显示数据点
                      lineStyle: {
                          color: colors[1]
                      },
                      areaStyle: {
                          color: new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                              offset: 0,
                              color: hexToRGBA(colors[1], 0.5)
                          }, {
                              offset: 1,
                              color: hexToRGBA(colors[1], 0.1)
                          }])
                      },
                      itemStyle: {
                        color: colors[1] // 设置总收入系列的图例颜色
                      }
                  }
              ]
          };

          // 使用刚指定的配置项和数据显示图表
          myChart.setOption(option);
          window.addEventListener("resize", () => {
            myChart.resize();
          });
        },
    }
});