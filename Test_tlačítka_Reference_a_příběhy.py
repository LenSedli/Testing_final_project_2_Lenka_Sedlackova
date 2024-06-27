def test_tlacitka_Reference_a_pribehy(page):
    page.goto('https://engeto.cz/')

    # Čekání na zobrazení tlačítka a kliknutí na něj
    accept_button = page.get_by_role("button", name="Chápu a přijímám!")
    accept_button.click()

    # Čekání na zobrazení tlačítka "Reference a příběhy"
    reference_a_pribehy = page.wait_for_selector('text="Reference a příběhy"', timeout=60000)

    # Ověření, že text tlačítka je "Reference a příběhy"
    assert reference_a_pribehy.inner_text().lower() == "reference a příběhy", "Text tlačítka není 'Reference a příběhy'"

    # Kliknutí na tlačítko "Reference a příběhy"
    reference_a_pribehy.click()