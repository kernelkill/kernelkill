# Como publicar o perfil `kernelkill`

1. Acesse https://github.com/new e crie um repositório **público** com o nome **kernelkill**, exatamente igual ao usuário (caso ele ainda não exista).
2. Extraia o ZIP e coloque `README.md` na raiz do repositório, com `assets/terminal-banner.svg` e `assets/status.svg` na subpasta `assets`.
3. No GitHub, use **Add file → Upload files**, envie os arquivos mantendo a estrutura, e clique em **Commit changes**. Para manter a estrutura com facilidade, também pode usar o terminal:

```bash
git clone https://github.com/kernelkill/kernelkill.git
cd kernelkill
# Copie o README.md e a pasta assets/ do ZIP para cá
git add README.md assets/
git commit -m "feat: add hacker terminal profile"
git push origin main
```

4. Acesse https://github.com/kernelkill e confira o resultado. O GitHub exibe automaticamente o README quando o repositório é público e tem o mesmo nome do usuário.

## Personalização

- Edite textos, certificações, tecnologias e links em `README.md`.
- Edite cores, títulos e animações em `assets/terminal-banner.svg` e `assets/status.svg` (SVGs locais, sem JS).
- **Importante:** os blocos de estatísticas e badges dependem de serviços externos (GitHub Readme Stats, DemoLab e Shields.io); podem ficar temporariamente indisponíveis. Os dois banners principais são arquivos próprios.
- Em telas pequenas, o texto extenso do SVG pode ser reduzido visualmente; todo o conteúdo essencial também aparece em texto acessível no README.
- Verifique no seu perfil as certificações e a descrição dos projetos antes de publicar; ajustes pessoais ficam sob seu controle.

Fonte oficial: https://docs.github.com/en/account-and-profile/how-tos/profile-customization/managing-your-profile-readme
