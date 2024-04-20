import React, { useState } from 'react';
import dynamic from "next/dynamic";
const Chart = dynamic(() => import("react-apexcharts"), { ssr: false });

import styles from './style.module.scss';

interface GraphProps {
  title?: string;
  value?: string;
  data: any;
  size?: 'small' | 'medium' | 'large';
  color?: string[];
}

const Graph = ({
  title,
  value,
  size = 'medium',
  data,
  color,
}: GraphProps) => {
  const [dataSample] = useState({
    options: {
      chart: {
        type: "bar",
        stacked: true,
        id: "basic-bar",
        group: "mixed",
        style: {
          color: "#4A4A4A",
          border: "1px solid #000",
          borderRadius: "5px",
        },
      },
      colors: color || ["#543de0"],
      dataLabels: {
        enabled: true,
        style: {
          fontSize: "12px",
          fontFamily: "var(--font)",
        },
      },
      plotOptions: {
        bar: {
          borderRadius: 4,
          horizontal: false,
          dataLabels: {
            total: {
              enabled: true,
              style: {
                fontSize: '12px',
                fontWeight: 900,
                fontFamily: "var(--font)",
                color: "#fdffff",
              }
            }
          }
        },
      },
      grid: {
        show: false,
      },
      xaxis: {
        show: false,
        labels: {
          style: {
            colors: "#0b1437",
          },
        },
      },
      yaxis: {
        show: false,
        labels: {
          style: {
            colors: "#0b1437",
          },
        },
      },
      legend: {
        show: true,
        fontSize: "15px",
        fontWeight: 600,
        position: "bottom",
        itemMargin: {
          horizontal: 10,
        },
        labels: {
          useSeriesColors: true,
        },
      },
      labels: data.map((item: any) => item.label),
    },
    series: [{
      name: "Series 1",
      data: data[0]?.value.map((item: any) => item),
    },
    {
      name: "Series 2",
      data: data[1]?.value.map((item: any) => item),
    },
    {
      name: "Series 3",
      data: data[2]?.value.map((item: any) => item),
    }]
  }) as any;

  if (!data) return null;

  return (
    <div className={styles.Graph_container} style={{
      width: size === 'small' ? '24%' : size === 'medium' ? '47%' : '100%',
      backgroundColor: '#111c44',
      borderRadius: '12px',
      padding: '20px',
    }}>
      <div className={styles.header}>
        <h2 className={styles.title}>{title}</h2>
        <h2 className={styles.value}>{value}</h2>
      </div>


      <Chart
          options={dataSample.options}
          series={dataSample.series}
          type="bar"
          width="100%"
          height={size === 'small' ? 70 : size === 'medium' ? 250 : 300}
        />
    </div>
  );
};

export default Graph;
