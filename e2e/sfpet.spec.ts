import { test, expect } from '@playwright/test';

test('spef', async ({ page }) => {
  await page.goto('https://sfpet.bmgf.io/');
  await page.getByRole('button', { name: 'Accept All' }).click();
  await page.getByRole('heading', { name: 'Subnational Family Planning Estimation Tool' }).click();
  await page.waitForLoadState('domcontentloaded');
  await page.locator('#chart1').hover();
  await page.locator('#chart2').hover();
  await page.getByLabel('Women 15-24, Parity 1+').hover();
  await page.getByRole('heading', { name: 'Women 15-24, Parity 0' }).click();
  await page.evaluate(() => {window.scrollBy(0, 1200); });
  await page.locator('#chart80').hover();
  
});