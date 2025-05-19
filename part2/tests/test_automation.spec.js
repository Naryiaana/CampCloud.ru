const {test, expect} = require('@playwright/test')

test('My first test ', async ({page}) => {

    await page.goto('https://example.com')

    await expect(page).toHaveTitle(/Example/)

    await page.locator('body > div > p:nth-child(3) > a').click()

    await expect(page).toHaveURL('https://www.iana.org/help/example-domains')
})