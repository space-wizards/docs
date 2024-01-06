# Grafana Dashboards

Contains the export for our Grafana dashboards at the time of writing. You will probably have to edit these to make them work with your server.

## Game Servers
```json
{
  "annotations": {
    "list": [
      {
        "builtIn": 1,
        "datasource": "-- Grafana --",
        "enable": true,
        "hide": true,
        "iconColor": "rgba(0, 211, 255, 1)",
        "name": "Annotations & Alerts",
        "target": {
          "limit": 100,
          "matchAny": false,
          "tags": [],
          "type": "dashboard"
        },
        "type": "dashboard"
      }
    ]
  },
  "editable": true,
  "fiscalYearStartMonth": 0,
  "graphTooltip": 0,
  "id": 1,
  "links": [],
  "liveNow": false,
  "panels": [
    {
      "aliasColors": {
        "wizards_den_eu_west": "blue"
      },
      "bars": false,
      "dashLength": 10,
      "dashes": false,
      "fieldConfig": {
        "defaults": {
          "links": []
        },
        "overrides": []
      },
      "fill": 3,
      "fillGradient": 0,
      "gridPos": {
        "h": 7,
        "w": 10,
        "x": 0,
        "y": 0
      },
      "hiddenSeries": false,
      "id": 2,
      "legend": {
        "avg": false,
        "current": false,
        "max": false,
        "min": false,
        "rightSide": false,
        "show": true,
        "total": false,
        "values": false
      },
      "lines": true,
      "linewidth": 2,
      "nullPointMode": "null",
      "options": {
        "alertThreshold": true
      },
      "percentage": false,
      "pluginVersion": "8.3.2",
      "pointradius": 2,
      "points": false,
      "renderer": "flot",
      "seriesOverrides": [],
      "spaceLength": 10,
      "stack": false,
      "steppedLine": true,
      "targets": [
        {
          "expr": "robust_player_count",
          "interval": "",
          "legendFormat": "{{job}}",
          "refId": "A"
        }
      ],
      "thresholds": [],
      "timeRegions": [],
      "title": "Player Count",
      "tooltip": {
        "shared": true,
        "sort": 0,
        "value_type": "individual"
      },
      "type": "graph",
      "xaxis": {
        "mode": "time",
        "show": true,
        "values": []
      },
      "yaxes": [
        {
          "decimals": 0,
          "format": "short",
          "logBase": 1,
          "min": "0",
          "show": true
        },
        {
          "format": "short",
          "logBase": 1,
          "show": true
        }
      ],
      "yaxis": {
        "align": false
      }
    },
    {
      "aliasColors": {
        "wizards_den_eu_west": "blue"
      },
      "bars": false,
      "dashLength": 10,
      "dashes": false,
      "fieldConfig": {
        "defaults": {
          "links": []
        },
        "overrides": []
      },
      "fill": 3,
      "fillGradient": 0,
      "gridPos": {
        "h": 7,
        "w": 10,
        "x": 10,
        "y": 0
      },
      "hiddenSeries": false,
      "id": 23,
      "legend": {
        "avg": false,
        "current": false,
        "max": false,
        "min": false,
        "rightSide": false,
        "show": true,
        "total": false,
        "values": false
      },
      "lines": true,
      "linewidth": 2,
      "nullPointMode": "null",
      "options": {
        "alertThreshold": true
      },
      "percentage": false,
      "pluginVersion": "8.3.2",
      "pointradius": 2,
      "points": false,
      "renderer": "flot",
      "seriesOverrides": [],
      "spaceLength": 10,
      "stack": false,
      "steppedLine": true,
      "targets": [
        {
          "exemplar": true,
          "expr": "sum(robust_player_count)",
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "thresholds": [],
      "timeRegions": [],
      "title": "Total Player Count",
      "tooltip": {
        "shared": true,
        "sort": 0,
        "value_type": "individual"
      },
      "type": "graph",
      "xaxis": {
        "mode": "time",
        "show": true,
        "values": []
      },
      "yaxes": [
        {
          "decimals": 0,
          "format": "short",
          "logBase": 1,
          "min": "0",
          "show": true
        },
        {
          "format": "short",
          "logBase": 1,
          "show": true
        }
      ],
      "yaxis": {
        "align": false
      }
    },
    {
      "alert": {
        "alertRuleTags": {},
        "conditions": [
          {
            "evaluator": {
              "params": [
                28
              ],
              "type": "lt"
            },
            "operator": {
              "type": "and"
            },
            "query": {
              "params": [
                "A",
                "1m",
                "now"
              ]
            },
            "reducer": {
              "params": [],
              "type": "median"
            },
            "type": "query"
          }
        ],
        "executionErrorState": "alerting",
        "for": "4m",
        "frequency": "1m",
        "handler": 1,
        "name": "TPS alert",
        "noDataState": "no_data",
        "notifications": [
          {
            "uid": "N5nihcmMk"
          }
        ]
      },
      "aliasColors": {
        "PlayerCount wizards_den_us_west": "dark-orange",
        "wizards_den_eu_west": "blue"
      },
      "bars": false,
      "dashLength": 10,
      "dashes": false,
      "fieldConfig": {
        "defaults": {
          "links": []
        },
        "overrides": []
      },
      "fill": 1,
      "fillGradient": 0,
      "gridPos": {
        "h": 6,
        "w": 10,
        "x": 0,
        "y": 7
      },
      "hiddenSeries": false,
      "id": 4,
      "legend": {
        "alignAsTable": false,
        "avg": false,
        "current": false,
        "max": false,
        "min": false,
        "rightSide": false,
        "show": true,
        "total": false,
        "values": false
      },
      "lines": true,
      "linewidth": 2,
      "nullPointMode": "null",
      "options": {
        "alertThreshold": true
      },
      "percentage": false,
      "pluginVersion": "8.3.2",
      "pointradius": 2,
      "points": false,
      "renderer": "flot",
      "seriesOverrides": [],
      "spaceLength": 10,
      "stack": false,
      "steppedLine": false,
      "targets": [
        {
          "expr": "rate(robust_server_curtick[30s])",
          "interval": "",
          "legendFormat": "{{job}}",
          "refId": "A"
        }
      ],
      "thresholds": [
        {
          "colorMode": "critical",
          "fill": true,
          "line": true,
          "op": "lt",
          "value": 28,
          "visible": true
        }
      ],
      "timeRegions": [],
      "title": "TPS",
      "tooltip": {
        "shared": true,
        "sort": 0,
        "value_type": "individual"
      },
      "type": "graph",
      "xaxis": {
        "mode": "time",
        "show": true,
        "values": []
      },
      "yaxes": [
        {
          "format": "hertz",
          "logBase": 1,
          "max": "35",
          "min": "0",
          "show": true
        },
        {
          "decimals": 0,
          "format": "short",
          "logBase": 1,
          "show": false
        }
      ],
      "yaxis": {
        "align": false
      }
    },
    {
      "aliasColors": {},
      "bars": false,
      "dashLength": 10,
      "dashes": false,
      "fieldConfig": {
        "defaults": {
          "links": []
        },
        "overrides": []
      },
      "fill": 1,
      "fillGradient": 0,
      "gridPos": {
        "h": 6,
        "w": 10,
        "x": 10,
        "y": 7
      },
      "hiddenSeries": false,
      "id": 12,
      "legend": {
        "avg": false,
        "current": false,
        "max": false,
        "min": false,
        "show": true,
        "total": false,
        "values": false
      },
      "lines": true,
      "linewidth": 1,
      "nullPointMode": "null",
      "options": {
        "alertThreshold": true
      },
      "percentage": false,
      "pluginVersion": "8.3.2",
      "pointradius": 2,
      "points": false,
      "renderer": "flot",
      "seriesOverrides": [],
      "spaceLength": 10,
      "stack": false,
      "steppedLine": false,
      "targets": [
        {
          "expr": "rate(process_cpu_seconds_total[10s])",
          "interval": "",
          "legendFormat": "{{job}}",
          "refId": "A"
        }
      ],
      "thresholds": [],
      "timeRegions": [],
      "title": "CPU Usage",
      "tooltip": {
        "shared": true,
        "sort": 0,
        "value_type": "individual"
      },
      "type": "graph",
      "xaxis": {
        "mode": "time",
        "show": true,
        "values": []
      },
      "yaxes": [
        {
          "decimals": 1,
          "format": "percentunit",
          "logBase": 1,
          "max": "1",
          "min": "0",
          "show": true
        },
        {
          "format": "short",
          "logBase": 1,
          "show": false
        }
      ],
      "yaxis": {
        "align": false
      }
    },
    {
      "alert": {
        "alertRuleTags": {},
        "conditions": [
          {
            "evaluator": {
              "params": [
                520850446
              ],
              "type": "gt"
            },
            "operator": {
              "type": "and"
            },
            "query": {
              "params": [
                "A",
                "1m",
                "now"
              ]
            },
            "reducer": {
              "params": [],
              "type": "max"
            },
            "type": "query"
          }
        ],
        "executionErrorState": "alerting",
        "for": "5m",
        "frequency": "1m",
        "handler": 1,
        "message": "Memory Usage Alert",
        "name": "Managed Memory alert",
        "noDataState": "no_data",
        "notifications": [
          {
            "uid": "N5nihcmMk"
          }
        ]
      },
      "aliasColors": {
        "wizards_den_eu_west": "blue"
      },
      "bars": false,
      "dashLength": 10,
      "dashes": false,
      "fieldConfig": {
        "defaults": {
          "links": []
        },
        "overrides": []
      },
      "fill": 1,
      "fillGradient": 0,
      "gridPos": {
        "h": 6,
        "w": 10,
        "x": 0,
        "y": 13
      },
      "hiddenSeries": false,
      "id": 9,
      "legend": {
        "avg": false,
        "current": false,
        "max": false,
        "min": false,
        "show": true,
        "total": false,
        "values": false
      },
      "lines": true,
      "linewidth": 1,
      "nullPointMode": "null",
      "options": {
        "alertThreshold": true
      },
      "percentage": false,
      "pluginVersion": "8.3.2",
      "pointradius": 2,
      "points": false,
      "renderer": "flot",
      "seriesOverrides": [],
      "spaceLength": 10,
      "stack": false,
      "steppedLine": false,
      "targets": [
        {
          "expr": "dotnet_total_memory_bytes",
          "format": "time_series",
          "interval": "",
          "legendFormat": "{{job}}",
          "refId": "A"
        }
      ],
      "thresholds": [
        {
          "colorMode": "critical",
          "fill": true,
          "line": true,
          "op": "gt",
          "value": 520850446,
          "visible": true
        }
      ],
      "timeRegions": [],
      "title": "Managed Memory",
      "tooltip": {
        "shared": true,
        "sort": 0,
        "value_type": "individual"
      },
      "type": "graph",
      "xaxis": {
        "mode": "time",
        "show": true,
        "values": []
      },
      "yaxes": [
        {
          "$$hashKey": "object:560",
          "format": "bytes",
          "logBase": 1,
          "min": "0",
          "show": true
        },
        {
          "$$hashKey": "object:561",
          "format": "short",
          "logBase": 1,
          "show": true
        }
      ],
      "yaxis": {
        "align": false
      }
    },
    {
      "description": "",
      "fieldConfig": {
        "defaults": {
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          },
          "unit": "dthms"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 5,
        "x": 10,
        "y": 13
      },
      "id": 6,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "last"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "auto"
      },
      "pluginVersion": "8.3.2",
      "targets": [
        {
          "exemplar": true,
          "expr": "ss14_round_length{job=\"wizards_den_lizard\"}",
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "US West Round Duration",
      "type": "stat"
    },
    {
      "description": "US west playercount",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "displayName": "Players",
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          },
          "unit": "none"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 2,
        "x": 15,
        "y": 13
      },
      "id": 15,
      "links": [],
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "center",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "last"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "auto"
      },
      "pluginVersion": "8.3.2",
      "targets": [
        {
          "expr": "robust_player_count",
          "format": "time_series",
          "instant": true,
          "interval": "",
          "legendFormat": "{{job}}",
          "refId": "A"
        }
      ],
      "title": "USW",
      "transformations": [
        {
          "id": "filterFieldsByName",
          "options": {
            "include": {
              "names": [
                "Time",
                "wizards_den_lizard"
              ]
            }
          }
        }
      ],
      "type": "stat"
    },
    {
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          }
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 2,
        "x": 18,
        "y": 13
      },
      "id": 25,
      "options": {
        "colorMode": "value",
        "graphMode": "area",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "auto"
      },
      "pluginVersion": "8.3.2",
      "targets": [
        {
          "exemplar": true,
          "expr": "sum(robust_player_count)",
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "Total Players",
      "type": "stat"
    },
    {
      "description": "",
      "fieldConfig": {
        "defaults": {
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          },
          "unit": "dthms"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 5,
        "x": 10,
        "y": 16
      },
      "id": 7,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "last"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "auto"
      },
      "pluginVersion": "8.3.2",
      "targets": [
        {
          "expr": "ss14_round_length{job=\"wizards_den_eu_west\"}",
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "EU West Round Duration",
      "type": "stat"
    },
    {
      "description": "EU west playercount",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "displayName": "Players",
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          },
          "unit": "none"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 2,
        "x": 15,
        "y": 16
      },
      "id": 16,
      "links": [],
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "center",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "last"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "auto"
      },
      "pluginVersion": "8.3.2",
      "targets": [
        {
          "expr": "robust_player_count",
          "format": "time_series",
          "instant": true,
          "interval": "",
          "legendFormat": "{{job}}",
          "refId": "A"
        }
      ],
      "title": "EUW",
      "transformations": [
        {
          "id": "filterFieldsByName",
          "options": {
            "include": {
              "names": [
                "Time",
                "wizards_den_eu_west"
              ]
            }
          }
        }
      ],
      "type": "stat"
    },
    {
      "aliasColors": {
        "wizards_den_eu_west": "blue"
      },
      "bars": false,
      "dashLength": 10,
      "dashes": false,
      "fieldConfig": {
        "defaults": {
          "links": []
        },
        "overrides": []
      },
      "fill": 1,
      "fillGradient": 0,
      "gridPos": {
        "h": 6,
        "w": 10,
        "x": 0,
        "y": 19
      },
      "hiddenSeries": false,
      "id": 22,
      "legend": {
        "avg": false,
        "current": false,
        "max": false,
        "min": false,
        "show": true,
        "total": false,
        "values": false
      },
      "lines": true,
      "linewidth": 1,
      "nullPointMode": "null as zero",
      "options": {
        "alertThreshold": true
      },
      "percentage": false,
      "pluginVersion": "8.3.2",
      "pointradius": 2,
      "points": false,
      "renderer": "flot",
      "seriesOverrides": [],
      "spaceLength": 10,
      "stack": false,
      "steppedLine": false,
      "targets": [
        {
          "expr": "robust_server_uptime",
          "format": "time_series",
          "interval": "",
          "legendFormat": "{{job}}",
          "refId": "A"
        }
      ],
      "thresholds": [],
      "timeRegions": [],
      "title": "Server Uptime",
      "tooltip": {
        "shared": true,
        "sort": 0,
        "value_type": "individual"
      },
      "type": "graph",
      "xaxis": {
        "mode": "time",
        "show": true,
        "values": []
      },
      "yaxes": [
        {
          "$$hashKey": "object:560",
          "format": "s",
          "logBase": 1,
          "min": "0",
          "show": true
        },
        {
          "$$hashKey": "object:561",
          "format": "short",
          "logBase": 1,
          "show": true
        }
      ],
      "yaxis": {
        "align": false
      }
    },
    {
      "description": "",
      "fieldConfig": {
        "defaults": {
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          },
          "unit": "dthms"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 5,
        "x": 10,
        "y": 19
      },
      "id": 13,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "last"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "auto"
      },
      "pluginVersion": "8.3.2",
      "targets": [
        {
          "expr": "ss14_round_length{job=\"wizards_den_eu_west_2\"}",
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "EU West 2 Round Duration",
      "type": "stat"
    },
    {
      "description": "EU west 2 playercount",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "displayName": "Players",
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          },
          "unit": "none"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 2,
        "x": 15,
        "y": 19
      },
      "id": 17,
      "links": [],
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "center",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "last"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "auto"
      },
      "pluginVersion": "8.3.2",
      "targets": [
        {
          "expr": "robust_player_count",
          "format": "time_series",
          "instant": true,
          "interval": "",
          "legendFormat": "{{job}}",
          "refId": "A"
        }
      ],
      "title": "EUW2",
      "transformations": [
        {
          "id": "filterFieldsByName",
          "options": {
            "include": {
              "names": [
                "Time",
                "wizards_den_eu_west_2"
              ]
            }
          }
        }
      ],
      "type": "stat"
    },
    {
      "description": "",
      "fieldConfig": {
        "defaults": {
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          },
          "unit": "dthms"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 5,
        "x": 10,
        "y": 22
      },
      "id": 10,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "last"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "auto"
      },
      "pluginVersion": "8.3.2",
      "targets": [
        {
          "expr": "ss14_round_length{job=\"wizards_den_centipede\"}",
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "Oceania Round Duration",
      "type": "stat"
    },
    {
      "description": "Oceania playercount",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "displayName": "Players",
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          },
          "unit": "none"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 2,
        "x": 15,
        "y": 22
      },
      "id": 18,
      "links": [],
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "center",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "last"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "auto"
      },
      "pluginVersion": "8.3.2",
      "targets": [
        {
          "expr": "robust_player_count",
          "format": "time_series",
          "instant": true,
          "interval": "",
          "legendFormat": "{{job}}",
          "refId": "A"
        }
      ],
      "title": "OCE",
      "transformations": [
        {
          "id": "filterFieldsByName",
          "options": {
            "include": {
              "names": [
                "Time",
                "wizards_den_centipede"
              ]
            }
          }
        }
      ],
      "type": "stat"
    },
    {
      "description": "",
      "fieldConfig": {
        "defaults": {
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          },
          "unit": "dthms"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 5,
        "x": 10,
        "y": 25
      },
      "id": 14,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "last"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "auto"
      },
      "pluginVersion": "8.3.2",
      "targets": [
        {
          "expr": "ss14_round_length{job=\"raspberry\"}",
          "instant": true,
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "Raspberry Round Duration",
      "type": "stat"
    },
    {
      "description": "Gradient/Raspberry playercount",
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "displayName": "Players",
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          },
          "unit": "none"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 3,
        "w": 2,
        "x": 15,
        "y": 25
      },
      "id": 19,
      "links": [],
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "center",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "last"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "auto"
      },
      "pluginVersion": "8.3.2",
      "targets": [
        {
          "expr": "robust_player_count",
          "format": "time_series",
          "instant": true,
          "interval": "",
          "legendFormat": "{{job}}",
          "refId": "A"
        }
      ],
      "title": "RSP",
      "transformations": [
        {
          "id": "filterFieldsByName",
          "options": {
            "include": {
              "names": [
                "raspberry",
                "Time"
              ]
            }
          }
        }
      ],
      "type": "stat"
    }
  ],
  "refresh": false,
  "schemaVersion": 33,
  "style": "dark",
  "tags": [
    "game servers"
  ],
  "templating": {
    "list": []
  },
  "time": {
    "from": "now-15m",
    "to": "now"
  },
  "timepicker": {
    "refresh_intervals": [
      "10s",
      "30s",
      "1m",
      "5m",
      "15m",
      "30m",
      "1h",
      "2h",
      "1d"
    ]
  },
  "timezone": "",
  "title": "Game Servers",
  "uid": "K0LTdKmMk",
  "version": 52,
  "weekStart": ""
}
```

## Perf Metrics

```json
{
  "annotations": {
    "list": [
      {
        "builtIn": 1,
        "datasource": "-- Grafana --",
        "enable": true,
        "hide": true,
        "iconColor": "rgba(0, 211, 255, 1)",
        "name": "Annotations & Alerts",
        "target": {
          "limit": 100,
          "matchAny": false,
          "tags": [],
          "type": "dashboard"
        },
        "type": "dashboard"
      }
    ]
  },
  "editable": true,
  "fiscalYearStartMonth": 0,
  "graphTooltip": 0,
  "id": 2,
  "iteration": 1640259621461,
  "links": [],
  "liveNow": false,
  "panels": [
    {
      "datasource": {
        "type": "loki",
        "uid": "DSc4tCGMk"
      },
      "description": "",
      "gridPos": {
        "h": 7,
        "w": 19,
        "x": 0,
        "y": 0
      },
      "id": 34,
      "options": {
        "dedupStrategy": "none",
        "enableLogDetails": true,
        "prettifyLogMessage": false,
        "showCommonLabels": false,
        "showLabels": false,
        "showTime": false,
        "sortOrder": "Descending",
        "wrapLogMessage": false
      },
      "targets": [
        {
          "expr": "{App=\"Robust.Server\",Server=\"$Server\"}",
          "refId": "A"
        }
      ],
      "title": "Logs",
      "transformations": [],
      "type": "logs"
    },
    {
      "collapsed": false,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 7
      },
      "id": 24,
      "panels": [],
      "title": "CPU",
      "type": "row"
    },
    {
      "aliasColors": {},
      "bars": false,
      "dashLength": 10,
      "dashes": false,
      "fieldConfig": {
        "defaults": {
          "links": []
        },
        "overrides": []
      },
      "fill": 1,
      "fillGradient": 0,
      "gridPos": {
        "h": 4,
        "w": 6,
        "x": 0,
        "y": 8
      },
      "hiddenSeries": false,
      "id": 13,
      "legend": {
        "avg": false,
        "current": false,
        "max": false,
        "min": false,
        "show": false,
        "total": false,
        "values": false
      },
      "lines": true,
      "linewidth": 1,
      "nullPointMode": "null",
      "options": {
        "alertThreshold": true
      },
      "percentage": false,
      "pluginVersion": "8.3.2",
      "pointradius": 2,
      "points": false,
      "renderer": "flot",
      "seriesOverrides": [],
      "spaceLength": 10,
      "stack": false,
      "steppedLine": false,
      "targets": [
        {
          "expr": "rate(process_cpu_seconds_total{job=\"$Server\"}[10s])",
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "thresholds": [],
      "timeRegions": [],
      "title": "CPU Usage",
      "tooltip": {
        "shared": true,
        "sort": 0,
        "value_type": "individual"
      },
      "type": "graph",
      "xaxis": {
        "mode": "time",
        "show": true,
        "values": []
      },
      "yaxes": [
        {
          "$$hashKey": "object:957",
          "decimals": 0,
          "format": "percentunit",
          "logBase": 1,
          "max": "1.05",
          "min": "0",
          "show": true
        },
        {
          "$$hashKey": "object:958",
          "format": "short",
          "logBase": 1,
          "show": false
        }
      ],
      "yaxis": {
        "align": false
      }
    },
    {
      "fieldConfig": {
        "defaults": {
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          },
          "unit": "dthms"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 4,
        "x": 6,
        "y": 8
      },
      "id": 15,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "last"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "auto"
      },
      "pluginVersion": "8.3.2",
      "targets": [
        {
          "expr": "robust_server_uptime{job=\"$Server\"}",
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "Uptime",
      "type": "stat"
    },
    {
      "fieldConfig": {
        "defaults": {
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              }
            ]
          },
          "unit": "dthms"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 4,
        "w": 4,
        "x": 10,
        "y": 8
      },
      "id": 16,
      "options": {
        "colorMode": "value",
        "graphMode": "none",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "last"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "auto"
      },
      "pluginVersion": "8.3.2",
      "targets": [
        {
          "expr": "robust_server_curtime{job=\"$Server\"}",
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "title": "CurTime",
      "type": "stat"
    },
    {
      "aliasColors": {},
      "bars": false,
      "dashLength": 10,
      "dashes": false,
      "fieldConfig": {
        "defaults": {
          "links": []
        },
        "overrides": []
      },
      "fill": 1,
      "fillGradient": 0,
      "gridPos": {
        "h": 4,
        "w": 5,
        "x": 14,
        "y": 8
      },
      "hiddenSeries": false,
      "id": 36,
      "legend": {
        "avg": false,
        "current": false,
        "max": false,
        "min": false,
        "show": false,
        "total": false,
        "values": false
      },
      "lines": true,
      "linewidth": 1,
      "nullPointMode": "null",
      "options": {
        "alertThreshold": true
      },
      "percentage": false,
      "pluginVersion": "8.3.2",
      "pointradius": 2,
      "points": false,
      "renderer": "flot",
      "seriesOverrides": [],
      "spaceLength": 10,
      "stack": false,
      "steppedLine": false,
      "targets": [
        {
          "expr": "robust_player_count{job=\"$Server\"}",
          "interval": "",
          "legendFormat": "{{job}}",
          "refId": "A"
        }
      ],
      "thresholds": [],
      "timeRegions": [],
      "title": "Player Count",
      "tooltip": {
        "shared": true,
        "sort": 0,
        "value_type": "individual"
      },
      "type": "graph",
      "xaxis": {
        "mode": "time",
        "show": true,
        "values": []
      },
      "yaxes": [
        {
          "$$hashKey": "object:145",
          "decimals": 0,
          "format": "short",
          "logBase": 1,
          "min": "0",
          "show": true
        },
        {
          "$$hashKey": "object:146",
          "format": "short",
          "logBase": 1,
          "show": false
        }
      ],
      "yaxis": {
        "align": false
      }
    },
    {
      "fieldConfig": {
        "defaults": {
          "color": {
            "mode": "thresholds"
          },
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 80
              }
            ]
          },
          "unit": "s"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 5,
        "x": 0,
        "y": 12
      },
      "id": 45,
      "options": {
        "displayMode": "gradient",
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "lastNotNull"
          ],
          "fields": "",
          "values": false
        },
        "showUnfilled": true,
        "text": {}
      },
      "pluginVersion": "8.3.2",
      "targets": [
        {
          "expr": "histogram_quantile(0.95, sum(rate(robust_entity_physics_controller_before_solve_bucket{job=\"$Server\"}[5m])) by (le, controller))",
          "interval": "",
          "legendFormat": "{{controller}}",
          "refId": "A"
        }
      ],
      "title": "Controller Tick Breakdown",
      "type": "bargauge"
    },
    {
      "cards": {},
      "color": {
        "cardColor": "#b4ff00",
        "colorScale": "sqrt",
        "colorScheme": "interpolateGreens",
        "exponent": 0.5,
        "mode": "opacity"
      },
      "dataFormat": "tsbuckets",
      "description": "How long gameloop ticks take.",
      "gridPos": {
        "h": 6,
        "w": 7,
        "x": 5,
        "y": 12
      },
      "heatmap": {},
      "hideZeroBuckets": false,
      "highlightCards": true,
      "id": 2,
      "legend": {
        "show": false
      },
      "reverseYBuckets": false,
      "targets": [
        {
          "expr": "rate(robust_game_loop_frametime_bucket{job=\"$Server\"}[10s])",
          "format": "heatmap",
          "interval": "",
          "legendFormat": "{{le}}",
          "refId": "A"
        }
      ],
      "title": "Tick Duration",
      "tooltip": {
        "show": true,
        "showHistogram": false
      },
      "type": "heatmap",
      "xAxis": {
        "show": true
      },
      "yAxis": {
        "decimals": 0,
        "format": "s",
        "logBase": 1,
        "show": true
      },
      "yBucketBound": "auto"
    },
    {
      "aliasColors": {},
      "bars": false,
      "dashLength": 10,
      "dashes": false,
      "fieldConfig": {
        "defaults": {
          "links": []
        },
        "overrides": []
      },
      "fill": 1,
      "fillGradient": 0,
      "gridPos": {
        "h": 6,
        "w": 7,
        "x": 12,
        "y": 12
      },
      "hiddenSeries": false,
      "id": 4,
      "legend": {
        "avg": false,
        "current": false,
        "max": false,
        "min": false,
        "show": false,
        "total": false,
        "values": false
      },
      "lines": true,
      "linewidth": 2,
      "nullPointMode": "null",
      "options": {
        "alertThreshold": true
      },
      "percentage": false,
      "pluginVersion": "8.3.2",
      "pointradius": 2,
      "points": false,
      "renderer": "flot",
      "seriesOverrides": [],
      "spaceLength": 10,
      "stack": false,
      "steppedLine": false,
      "targets": [
        {
          "expr": "rate(robust_server_curtick{job=\"$Server\"}[10s])",
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "thresholds": [],
      "timeRegions": [],
      "title": "Tickrate",
      "tooltip": {
        "shared": true,
        "sort": 0,
        "value_type": "individual"
      },
      "type": "graph",
      "xaxis": {
        "mode": "time",
        "show": true,
        "values": []
      },
      "yaxes": [
        {
          "$$hashKey": "object:350",
          "format": "hertz",
          "logBase": 1,
          "show": true
        },
        {
          "$$hashKey": "object:351",
          "format": "short",
          "logBase": 1,
          "show": true
        }
      ],
      "yaxis": {
        "align": false
      }
    },
    {
      "fieldConfig": {
        "defaults": {
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 0.001
              }
            ]
          },
          "unit": "s"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 8,
        "w": 7,
        "x": 5,
        "y": 18
      },
      "id": 41,
      "options": {
        "displayMode": "gradient",
        "orientation": "horizontal",
        "reduceOptions": {
          "calcs": [
            "mean"
          ],
          "fields": "",
          "values": true
        },
        "showUnfilled": true,
        "text": {}
      },
      "pluginVersion": "8.3.2",
      "targets": [
        {
          "expr": "topk(10, histogram_quantile(0.95, sum(rate(robust_entity_systems_update_usage_bucket{job=\"$Server\"}[5m])) by (le, system)))",
          "format": "time_series",
          "instant": true,
          "interval": "",
          "legendFormat": "{{system}}",
          "refId": "A"
        }
      ],
      "title": "95% System Tick Breakdown",
      "transformations": [],
      "type": "bargauge"
    },
    {
      "aliasColors": {},
      "breakPoint": "50%",
      "combine": {
        "label": "Others",
        "threshold": 0
      },
      "decimals": 0,
      "fontSize": "80%",
      "format": "s",
      "gridPos": {
        "h": 8,
        "w": 7,
        "x": 12,
        "y": 18
      },
      "id": 39,
      "legend": {
        "percentage": true,
        "show": true,
        "sort": "current",
        "sortDesc": true,
        "values": true
      },
      "legendType": "Right side",
      "links": [],
      "nullPointMode": "connected",
      "pieType": "pie",
      "pluginVersion": "7.1.5",
      "strokeWidth": "0.25",
      "targets": [
        {
          "expr": "histogram_quantile(0.95, sum(rate(robust_server_update_usage_bucket[1m])) by (le, area))",
          "interval": "",
          "legendFormat": "{{area}}",
          "refId": "A"
        }
      ],
      "title": "95% Main Tick Timing",
      "type": "grafana-piechart-panel",
      "valueName": "current"
    },
    {
      "aliasColors": {},
      "breakPoint": "50%",
      "combine": {
        "label": "Others",
        "threshold": 0
      },
      "description": "",
      "fontSize": "50%",
      "format": "s",
      "gridPos": {
        "h": 6,
        "w": 5,
        "x": 0,
        "y": 20
      },
      "id": 43,
      "legend": {
        "header": "",
        "show": false,
        "sideWidth": 10,
        "values": true
      },
      "legendType": "On graph",
      "links": [],
      "nullPointMode": "connected",
      "pieType": "pie",
      "pluginVersion": "7.3.2",
      "strokeWidth": "1",
      "targets": [
        {
          "expr": "topk(10, histogram_quantile(0.95, sum(rate(robust_entity_systems_update_usage_bucket{job=\"$Server\"}[5m])) by (le, system)))",
          "interval": "",
          "legendFormat": "{{system}}",
          "refId": "A"
        }
      ],
      "title": "95% System Tick Chart",
      "type": "grafana-piechart-panel",
      "valueName": "current"
    },
    {
      "collapsed": false,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 26
      },
      "id": 22,
      "panels": [],
      "title": "Network",
      "type": "row"
    },
    {
      "aliasColors": {
        "Send": "blue"
      },
      "bars": false,
      "dashLength": 10,
      "dashes": false,
      "description": "",
      "fieldConfig": {
        "defaults": {
          "links": []
        },
        "overrides": []
      },
      "fill": 1,
      "fillGradient": 0,
      "gridPos": {
        "h": 6,
        "w": 7,
        "x": 0,
        "y": 27
      },
      "hiddenSeries": false,
      "id": 6,
      "legend": {
        "avg": false,
        "current": false,
        "max": false,
        "min": false,
        "show": true,
        "total": false,
        "values": false
      },
      "lines": true,
      "linewidth": 2,
      "nullPointMode": "null",
      "options": {
        "alertThreshold": true
      },
      "percentage": false,
      "pluginVersion": "8.3.2",
      "pointradius": 2,
      "points": false,
      "renderer": "flot",
      "seriesOverrides": [],
      "spaceLength": 10,
      "stack": false,
      "steppedLine": false,
      "targets": [
        {
          "expr": "rate(robust_net_recv_bytes{job=\"$Server\"}[10s])",
          "interval": "",
          "legendFormat": "Receive",
          "refId": "A"
        },
        {
          "expr": "rate(robust_net_sent_bytes{job=\"$Server\"}[10s])",
          "interval": "",
          "legendFormat": "Send",
          "refId": "B"
        }
      ],
      "thresholds": [],
      "timeRegions": [],
      "title": "Network Usage",
      "tooltip": {
        "shared": true,
        "sort": 0,
        "value_type": "individual"
      },
      "type": "graph",
      "xaxis": {
        "mode": "time",
        "show": true,
        "values": []
      },
      "yaxes": [
        {
          "$$hashKey": "object:268",
          "decimals": 0,
          "format": "Bps",
          "logBase": 1,
          "min": "0",
          "show": true
        },
        {
          "$$hashKey": "object:269",
          "format": "short",
          "logBase": 1,
          "show": false
        }
      ],
      "yaxis": {
        "align": false
      }
    },
    {
      "aliasColors": {
        "Receive Messages": "dark-red",
        "Receive Packets": "red",
        "Send": "blue",
        "Send Messages": "semi-dark-blue",
        "Send Packets": "blue"
      },
      "bars": false,
      "dashLength": 10,
      "dashes": false,
      "description": "* Packets: real UDP packets.\n* Messages: Lidgren messages.\n\nLidgren can combine multiple messages into one UDP packet so these numbers are not necessarily equal.  ",
      "fieldConfig": {
        "defaults": {
          "links": []
        },
        "overrides": []
      },
      "fill": 1,
      "fillGradient": 0,
      "gridPos": {
        "h": 6,
        "w": 7,
        "x": 7,
        "y": 27
      },
      "hiddenSeries": false,
      "id": 7,
      "legend": {
        "avg": false,
        "current": false,
        "max": false,
        "min": false,
        "show": true,
        "total": false,
        "values": false
      },
      "lines": true,
      "linewidth": 2,
      "nullPointMode": "null",
      "options": {
        "alertThreshold": true
      },
      "percentage": false,
      "pluginVersion": "8.3.2",
      "pointradius": 2,
      "points": false,
      "renderer": "flot",
      "seriesOverrides": [],
      "spaceLength": 10,
      "stack": false,
      "steppedLine": false,
      "targets": [
        {
          "expr": "rate(robust_net_recv_packets{job=\"$Server\"}[10s])",
          "interval": "",
          "legendFormat": "Receive Packets",
          "refId": "A"
        },
        {
          "expr": "rate(robust_net_sent_packets{job=\"$Server\"}[10s])",
          "interval": "",
          "legendFormat": "Send Packets",
          "refId": "B"
        },
        {
          "expr": "rate(robust_net_sent_messages{job=\"$Server\"}[10s])",
          "interval": "",
          "legendFormat": "Send Messages",
          "refId": "C"
        },
        {
          "expr": "rate(robust_net_recv_messages{job=\"$Server\"}[10s])",
          "interval": "",
          "legendFormat": "Receive Messages",
          "refId": "D"
        }
      ],
      "thresholds": [],
      "timeRegions": [],
      "title": "Packets",
      "tooltip": {
        "shared": true,
        "sort": 0,
        "value_type": "individual"
      },
      "type": "graph",
      "xaxis": {
        "mode": "time",
        "show": true,
        "values": []
      },
      "yaxes": [
        {
          "$$hashKey": "object:268",
          "decimals": 0,
          "format": "pps",
          "logBase": 1,
          "min": "0",
          "show": true
        },
        {
          "$$hashKey": "object:269",
          "format": "short",
          "logBase": 1,
          "show": false
        }
      ],
      "yaxis": {
        "align": false
      }
    },
    {
      "aliasColors": {},
      "bars": false,
      "dashLength": 10,
      "dashes": false,
      "description": "How many messages are currently stored by Lidgren.\n\n* Stored: Reliable messages that are stored in case they need to be re-sent.\n* Unsent: Messages that have not yet been sent because of network overload.",
      "fieldConfig": {
        "defaults": {
          "links": []
        },
        "overrides": []
      },
      "fill": 1,
      "fillGradient": 0,
      "gridPos": {
        "h": 5,
        "w": 6,
        "x": 0,
        "y": 33
      },
      "hiddenSeries": false,
      "id": 28,
      "legend": {
        "avg": false,
        "current": false,
        "max": false,
        "min": false,
        "show": true,
        "total": false,
        "values": false
      },
      "lines": true,
      "linewidth": 1,
      "nullPointMode": "null",
      "options": {
        "alertThreshold": true
      },
      "percentage": false,
      "pluginVersion": "8.3.2",
      "pointradius": 2,
      "points": false,
      "renderer": "flot",
      "seriesOverrides": [],
      "spaceLength": 10,
      "stack": false,
      "steppedLine": false,
      "targets": [
        {
          "expr": "robust_net_stored{job=\"$Server\"}",
          "interval": "",
          "legendFormat": "Stored",
          "refId": "A"
        },
        {
          "expr": "robust_net_unsent{job=\"$Server\"}",
          "interval": "",
          "legendFormat": "Unsent",
          "refId": "B"
        }
      ],
      "thresholds": [],
      "timeRegions": [],
      "title": "Stored Messages",
      "tooltip": {
        "shared": true,
        "sort": 0,
        "value_type": "individual"
      },
      "type": "graph",
      "xaxis": {
        "mode": "time",
        "show": true,
        "values": []
      },
      "yaxes": [
        {
          "$$hashKey": "object:134",
          "decimals": 0,
          "format": "none",
          "logBase": 1,
          "min": "0",
          "show": true
        },
        {
          "$$hashKey": "object:135",
          "format": "short",
          "logBase": 1,
          "show": false
        }
      ],
      "yaxis": {
        "align": false
      }
    },
    {
      "aliasColors": {},
      "bars": false,
      "dashLength": 10,
      "dashes": false,
      "description": "How many reliable messages are being re-sent by Lidgren.",
      "fieldConfig": {
        "defaults": {
          "links": []
        },
        "overrides": []
      },
      "fill": 1,
      "fillGradient": 0,
      "gridPos": {
        "h": 5,
        "w": 6,
        "x": 6,
        "y": 33
      },
      "hiddenSeries": false,
      "id": 30,
      "legend": {
        "avg": false,
        "current": false,
        "max": false,
        "min": false,
        "show": true,
        "total": false,
        "values": false
      },
      "lines": true,
      "linewidth": 1,
      "nullPointMode": "null",
      "options": {
        "alertThreshold": true
      },
      "percentage": false,
      "pluginVersion": "8.3.2",
      "pointradius": 2,
      "points": false,
      "renderer": "flot",
      "seriesOverrides": [],
      "spaceLength": 10,
      "stack": false,
      "steppedLine": false,
      "targets": [
        {
          "expr": "rate(robust_net_resent_delay{job=\"$Server\"}[10s])",
          "interval": "",
          "legendFormat": "Delay",
          "refId": "A"
        },
        {
          "expr": "rate(robust_net_resent_hole{job=\"$Server\"}[10s])",
          "interval": "",
          "legendFormat": "Holes",
          "refId": "B"
        }
      ],
      "thresholds": [],
      "timeRegions": [],
      "title": "Resent Messages",
      "tooltip": {
        "shared": true,
        "sort": 0,
        "value_type": "individual"
      },
      "type": "graph",
      "xaxis": {
        "mode": "time",
        "show": true,
        "values": []
      },
      "yaxes": [
        {
          "$$hashKey": "object:614",
          "decimals": 0,
          "format": "short",
          "logBase": 1,
          "min": "0",
          "show": true
        },
        {
          "$$hashKey": "object:615",
          "format": "short",
          "logBase": 1,
          "show": true
        }
      ],
      "yaxis": {
        "align": false
      }
    },
    {
      "aliasColors": {},
      "bars": false,
      "dashLength": 10,
      "dashes": false,
      "description": "How many messages are getting dropped by Lidgren. This usually indicates duplicates or sequencing issues.",
      "fieldConfig": {
        "defaults": {
          "links": []
        },
        "overrides": []
      },
      "fill": 1,
      "fillGradient": 0,
      "gridPos": {
        "h": 5,
        "w": 6,
        "x": 12,
        "y": 33
      },
      "hiddenSeries": false,
      "id": 32,
      "legend": {
        "avg": false,
        "current": false,
        "max": false,
        "min": false,
        "show": false,
        "total": false,
        "values": false
      },
      "lines": true,
      "linewidth": 1,
      "nullPointMode": "null",
      "options": {
        "alertThreshold": true
      },
      "percentage": false,
      "pluginVersion": "8.3.2",
      "pointradius": 2,
      "points": false,
      "renderer": "flot",
      "seriesOverrides": [],
      "spaceLength": 10,
      "stack": false,
      "steppedLine": false,
      "targets": [
        {
          "expr": "rate(robust_net_dropped{job=\"$Server\"}[10s])",
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "thresholds": [],
      "timeRegions": [],
      "title": "Dropped Messages",
      "tooltip": {
        "shared": true,
        "sort": 0,
        "value_type": "individual"
      },
      "type": "graph",
      "xaxis": {
        "mode": "time",
        "show": true,
        "values": []
      },
      "yaxes": [
        {
          "$$hashKey": "object:701",
          "decimals": 0,
          "format": "short",
          "logBase": 1,
          "min": "0",
          "show": true
        },
        {
          "$$hashKey": "object:702",
          "format": "short",
          "logBase": 1,
          "show": false
        }
      ],
      "yaxis": {
        "align": false
      }
    },
    {
      "collapsed": false,
      "gridPos": {
        "h": 1,
        "w": 24,
        "x": 0,
        "y": 38
      },
      "id": 20,
      "panels": [],
      "title": "Memory",
      "type": "row"
    },
    {
      "description": "How often the GC is running, by generation.",
      "fieldConfig": {
        "defaults": {
          "mappings": [],
          "thresholds": {
            "mode": "absolute",
            "steps": [
              {
                "color": "green",
                "value": null
              },
              {
                "color": "red",
                "value": 1.5
              }
            ]
          },
          "unit": "none"
        },
        "overrides": []
      },
      "gridPos": {
        "h": 5,
        "w": 14,
        "x": 0,
        "y": 39
      },
      "id": 18,
      "options": {
        "colorMode": "value",
        "graphMode": "area",
        "justifyMode": "auto",
        "orientation": "auto",
        "reduceOptions": {
          "calcs": [
            "last"
          ],
          "fields": "",
          "values": false
        },
        "text": {},
        "textMode": "auto"
      },
      "pluginVersion": "8.3.2",
      "targets": [
        {
          "expr": "rate(dotnet_collection_count_total{job=\"$Server\"}[1m])",
          "interval": "",
          "legendFormat": "{{generation}}",
          "refId": "A"
        }
      ],
      "title": "GC Per Minute",
      "type": "stat"
    },
    {
      "aliasColors": {},
      "bars": false,
      "dashLength": 10,
      "dashes": false,
      "description": "Managed and working set memory",
      "fieldConfig": {
        "defaults": {
          "links": []
        },
        "overrides": []
      },
      "fill": 1,
      "fillGradient": 0,
      "gridPos": {
        "h": 5,
        "w": 6,
        "x": 0,
        "y": 44
      },
      "hiddenSeries": false,
      "id": 9,
      "legend": {
        "avg": false,
        "current": false,
        "max": false,
        "min": false,
        "show": false,
        "total": false,
        "values": false
      },
      "lines": true,
      "linewidth": 2,
      "nullPointMode": "null",
      "options": {
        "alertThreshold": true
      },
      "percentage": false,
      "pluginVersion": "8.3.2",
      "pointradius": 2,
      "points": false,
      "renderer": "flot",
      "seriesOverrides": [],
      "spaceLength": 10,
      "stack": true,
      "steppedLine": false,
      "targets": [
        {
          "exemplar": true,
          "expr": "dotnet_total_memory_bytes{job=\"$Server\"}",
          "interval": "",
          "legendFormat": "Managed memory",
          "refId": "A"
        },
        {
          "exemplar": true,
          "expr": "process_working_set_bytes{job=\"$Server\"}-dotnet_total_memory_bytes{job=\"$Server\"}",
          "hide": false,
          "interval": "",
          "legendFormat": "Working Set (Extra)",
          "refId": "B"
        }
      ],
      "thresholds": [],
      "timeRegions": [],
      "title": "Memory",
      "tooltip": {
        "shared": true,
        "sort": 0,
        "value_type": "individual"
      },
      "type": "graph",
      "xaxis": {
        "mode": "time",
        "show": true,
        "values": []
      },
      "yaxes": [
        {
          "$$hashKey": "object:449",
          "format": "bytes",
          "logBase": 1,
          "min": "0",
          "show": true
        },
        {
          "$$hashKey": "object:450",
          "format": "short",
          "logBase": 1,
          "show": false
        }
      ],
      "yaxis": {
        "align": false
      }
    },
    {
      "aliasColors": {},
      "bars": false,
      "dashLength": 10,
      "dashes": false,
      "fieldConfig": {
        "defaults": {
          "links": []
        },
        "overrides": []
      },
      "fill": 1,
      "fillGradient": 0,
      "gridPos": {
        "h": 5,
        "w": 6,
        "x": 6,
        "y": 44
      },
      "hiddenSeries": false,
      "id": 11,
      "legend": {
        "avg": false,
        "current": false,
        "max": false,
        "min": false,
        "show": false,
        "total": false,
        "values": false
      },
      "lines": true,
      "linewidth": 2,
      "nullPointMode": "null",
      "options": {
        "alertThreshold": true
      },
      "percentage": false,
      "pluginVersion": "8.3.2",
      "pointradius": 2,
      "points": false,
      "renderer": "flot",
      "seriesOverrides": [],
      "spaceLength": 10,
      "stack": false,
      "steppedLine": false,
      "targets": [
        {
          "expr": "robust_entities_count{job=\"$Server\"}",
          "interval": "",
          "legendFormat": "",
          "refId": "A"
        }
      ],
      "thresholds": [],
      "timeRegions": [],
      "title": "Game Entity Count",
      "tooltip": {
        "shared": true,
        "sort": 0,
        "value_type": "individual"
      },
      "type": "graph",
      "xaxis": {
        "mode": "time",
        "show": true,
        "values": []
      },
      "yaxes": [
        {
          "$$hashKey": "object:678",
          "format": "short",
          "logBase": 1,
          "min": "0",
          "show": true
        },
        {
          "$$hashKey": "object:679",
          "format": "short",
          "logBase": 1,
          "show": true
        }
      ],
      "yaxis": {
        "align": false
      }
    }
  ],
  "refresh": false,
  "schemaVersion": 33,
  "style": "dark",
  "tags": [
    "game servers"
  ],
  "templating": {
    "list": [
      {
        "current": {
          "selected": true,
          "text": "wizards_den_eu_west",
          "value": "wizards_den_eu_west"
        },
        "hide": 0,
        "includeAll": false,
        "multi": false,
        "name": "Server",
        "options": [
          {
            "selected": true,
            "text": "wizards_den_eu_west",
            "value": "wizards_den_eu_west"
          },
          {
            "selected": false,
            "text": "wizards_den_lizard",
            "value": "wizards_den_lizard"
          },
          {
            "selected": false,
            "text": "raspberry",
            "value": "raspberry"
          },
          {
            "selected": false,
            "text": "wizards_den_eu_west_2",
            "value": "wizards_den_eu_west_2"
          },
          {
            "selected": false,
            "text": "wizards_den_centipede",
            "value": "wizards_den_centipede"
          }
        ],
        "query": "wizards_den_eu_west, wizards_den_lizard, raspberry, wizards_den_eu_west_2, wizards_den_centipede",
        "queryValue": "",
        "skipUrlSync": false,
        "type": "custom"
      }
    ]
  },
  "time": {
    "from": "now-15m",
    "to": "now"
  },
  "timepicker": {
    "refresh_intervals": [
      "10s",
      "30s",
      "1m",
      "5m",
      "15m",
      "30m",
      "1h",
      "2h",
      "1d"
    ]
  },
  "timezone": "",
  "title": "Perf Metrics",
  "uid": "qyFqpFiGk",
  "version": 44,
  "weekStart": ""
}
```