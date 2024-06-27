def test_tlacitka_Do_portalu(page):
    page.goto('https://engeto.cz/')

    # Čekání na zobrazení tlačítka a kliknutí na něj
    accept_button = page.get_by_role("button", name="Chápu a přijímám!")
    accept_button.click()

    # Čekání na zobrazení tlačítka "Do portálu"
    do_portalu = page.wait_for_selector('a.portal-link.h6.is_bold_700[href="https://learn.engeto.com/cs/prihlaseni"]')

    # Ověření, že text tlačítka je "Do portálu"
    assert do_portalu.inner_text() == "Do portálu", "Text tlačítka není 'Do portálu'"

    # Kliknutí na tlačítko "Do portálu"
    do_portalu.click()


