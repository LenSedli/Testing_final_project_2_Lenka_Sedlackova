def test_tlacitka_Terminy(page):
    page.goto('https://engeto.cz/')

    # Čekání na zobrazení tlačítka a kliknutí na něj
    accept_button = page.get_by_role("button", name="Chápu a přijímám!")
    accept_button.click()

    # Čekání na zobrazení tlačítka "Termíny"
    terminy = page.wait_for_selector('a[href="/#terminy"]')

    # Ověření, že text tlačítka je "Termíny"
    assert terminy.inner_text() == "Termíny", "Text tlačítka není 'Termíny'"

    # Kliknutí na tlačítko "Termíny"
    terminy.click()

