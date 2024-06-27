def test_tlacitka_Terminy(page):
    page.goto('https://engeto.cz/')

    # Čekání na zobrazení tlačítka a kliknutí na něj
    accept_button = page.get_by_role("button", name="Chápu a přijímám!")
    accept_button.click()

    # Čekání na zobrazení tlačítka "Termíny"
    terminy = page.wait_for_selector('.block-button.type-premium.size-l.orange-link.hide-mobile')

    # Ověření, že text tlačítka je "Termíny"
    assert terminy.inner_text().lower() == "termíny".lower(), "Text tlačítka není 'Termíny'"

    # Kliknutí na tlačítko "Termíny"
    terminy.click()

