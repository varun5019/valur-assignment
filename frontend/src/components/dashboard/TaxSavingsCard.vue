<script setup lang="ts">
import { ref, computed } from 'vue'
import { Line } from 'vue-chartjs'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Filler,
} from 'chart.js'
import BaseIcon from '../ui/BaseIcon.vue'

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Filler
)

const selectedMonth = ref('Mar')
const months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul']

const chartData = computed(() => ({
  labels: months,
  datasets: [
    {
      data: [2000, 3500, 5000, 4200, 4800, 5200, 5500],
      borderColor: '#3D6ED8',
      backgroundColor: (context: any) => {
        const chart = context.chart
        const { ctx, chartArea } = chart
        if (!chartArea) return 'rgba(61, 110, 216, 0.1)'
        const gradient = ctx.createLinearGradient(0, chartArea.top, 0, chartArea.bottom)
        gradient.addColorStop(0, 'rgba(61, 110, 216, 0.2)')
        gradient.addColorStop(1, 'rgba(61, 110, 216, 0.02)')
        return gradient
      },
      fill: true,
      tension: 0.4,
      borderWidth: 2,
      pointRadius: months.map(m => m === selectedMonth.value ? 8 : 0),
      pointBackgroundColor: '#3D6ED8',
      pointBorderColor: 'white',
      pointBorderWidth: 3,
      pointHoverRadius: 8,
    },
  ],
}))

const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      display: false,
    },
    tooltip: {
      enabled: false,
    },
  },
  scales: {
    x: {
      display: false,
    },
    y: {
      display: false,
    },
  },
  interaction: {
    intersect: false,
    mode: 'index' as const,
  },
}
</script>

<template>
  <div class="tax-savings-card">
    <div class="tax-savings-card__header">
      <div class="tax-savings-card__info">
        <span class="tax-savings-card__label">Tax Savings</span>
        <div class="tax-savings-card__value">
          <span class="tax-savings-card__amount">$11,756</span>
          <div class="tax-savings-card__change">
            <svg width="12" height="12" viewBox="0 0 12 12" fill="none">
              <path d="M6 2L10 6H7V10H5V6H2L6 2Z" fill="#22C55E"/>
            </svg>
            <span>12.75%</span>
          </div>
        </div>
      </div>
      <div class="tax-savings-card__actions">
        <button class="tax-savings-card__dropdown">
          <span>Last 6 months</span>
          <BaseIcon name="chevron-down" :size="20" />
        </button>
        <button class="tax-savings-card__more">
          <BaseIcon name="more" :size="20" />
        </button>
      </div>
    </div>

    <div class="tax-savings-card__divider"></div>

    <div class="tax-savings-card__chart">
      <div class="tax-savings-card__tooltip" v-if="selectedMonth === 'Mar'">
        <span class="tax-savings-card__tooltip-value">$5k</span>
        <div class="tax-savings-card__tooltip-arrow"></div>
      </div>
      <Line :data="chartData" :options="chartOptions" />
    </div>

    <div class="tax-savings-card__months">
      <span
        v-for="month in months"
        :key="month"
        class="tax-savings-card__month"
      >
        {{ month }}
      </span>
    </div>
  </div>
</template>

<style scoped>
.tax-savings-card {
  background: var(--surface-card-bg);
  border-radius: 20px;
  border: 1px solid var(--outline-button-neutral);
  padding: 24px;
  display: flex;
  flex-direction: column;
  gap: 26px;
}

.tax-savings-card__header {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
}

.tax-savings-card__info {
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.tax-savings-card__label {
  font-family: var(--font-family);
  font-size: 18px;
  font-weight: 400;
  color: var(--text-secondary);
}

.tax-savings-card__value {
  display: flex;
  align-items: flex-end;
  gap: 4px;
}

.tax-savings-card__amount {
  font-family: var(--font-family);
  font-size: 22px;
  font-weight: 600;
  color: var(--text-primary);
}

.tax-savings-card__change {
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 1px 0;
  font-family: var(--font-family);
  font-size: 16px;
  font-weight: 400;
  color: var(--text-success);
}

.tax-savings-card__actions {
  display: flex;
  align-items: center;
  gap: 8px;
}

.tax-savings-card__dropdown {
  display: flex;
  align-items: center;
  gap: 4px;
  background: var(--surface-button-secondary-bg);
  border: 1px solid var(--outline-button-neutral);
  border-radius: 8px;
  padding: 8px;
  font-family: var(--font-family);
  font-size: 12px;
  font-weight: 500;
  color: var(--text-primary);
  cursor: pointer;
  transition: background 0.15s ease;
}

.tax-savings-card__dropdown:hover {
  background: var(--color-neutral-50);
}

.tax-savings-card__more {
  display: flex;
  align-items: center;
  justify-content: center;
  background: var(--surface-button-secondary-bg);
  border: 1px solid var(--outline-button-neutral);
  border-radius: 8px;
  padding: 8px;
  color: var(--text-primary);
  cursor: pointer;
  transition: background 0.15s ease;
}

.tax-savings-card__more:hover {
  background: var(--color-neutral-50);
}

.tax-savings-card__divider {
  height: 1px;
  background: var(--outline-button-neutral);
  width: 100%;
}

.tax-savings-card__chart {
  position: relative;
  height: 170px;
}

.tax-savings-card__tooltip {
  position: absolute;
  top: 60px;
  left: 152px;
  background: var(--surface-card-bg);
  border: 1px solid var(--outline-button-neutral);
  border-radius: 8px;
  padding: 8px 12px;
  box-shadow: 0 2px 16px rgba(13, 10, 44, 0.12);
  z-index: 10;
}

.tax-savings-card__tooltip-value {
  font-family: var(--font-family);
  font-size: 16px;
  font-weight: 500;
  color: var(--text-primary);
}

.tax-savings-card__tooltip-arrow {
  position: absolute;
  bottom: -6px;
  left: 50%;
  transform: translateX(-50%);
  width: 10px;
  height: 10px;
  background: var(--surface-card-bg);
  border-right: 1px solid var(--outline-button-neutral);
  border-bottom: 1px solid var(--outline-button-neutral);
  transform: translateX(-50%) rotate(45deg);
}

.tax-savings-card__months {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.tax-savings-card__month {
  font-family: var(--font-family);
  font-size: 16px;
  font-weight: 400;
  color: var(--text-secondary);
  text-align: center;
}
</style>
