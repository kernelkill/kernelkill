# KERNELKILL — Hacker Terminal V2

## 1. Atualizar o perfil existente

O perfil já usa o repositório especial `https://github.com/kernelkill/kernelkill`.
Substitua o README e envie `assets/`, `scripts/` e `.github/workflows/` preservando os caminhos.

### Via terminal

```bash
git clone https://github.com/kernelkill/kernelkill.git
cd kernelkill
# Copie os arquivos da pasta kernelkill-v2 aqui, inclusive a pasta oculta .github
git add README.md assets scripts .github/workflows/profile-metrics.yml
git commit -m 'feat: profile hacker terminal v2'
git push origin main
```

## 2. Iniciar a telemetria

- Acesse `https://github.com/kernelkill/kernelkill/actions`.
- Em **Update profile telemetry**, clique em **Run workflow**.
- O workflow gera `assets/github-metrics.svg`, que aparecerá no README após o primeiro run bem-sucedido.
- O arquivo é atualizado diariamente. Caso falhe com erro 403 ao fazer push, em Settings > Actions > General > Workflow permissions, selecione **Read and write permissions**, se permitido nas configurações da conta.
- Se GitHub Actions estiver desativado, habilite-o para o repositório.
- Não é necessário criar Personal Access Token ou revelar credenciais.

## 3. Editar a bio lateral (não é controlada pelo README)

Perfil > **Edit profile** > campo **Bio**:

`Cybersecurity Researcher | Red Team & AppSec | Bug Bounty | Fortinet/F5 | AI Security Automation`

Website: `https://kachorroskicyber.com`

## 4. Fixar os repositórios

No perfil, desça até **Pinned** / **Popular repositories**, clique em **Customize your pins** e escolha até seis repositórios públicos. Priorize `CaidoAIDriven` e outros trabalhos de cybersecurity publicados; evite fixar repositórios de aula antigos se não forem relevantes. É possível mudar a ordem arrastando os cards.

## 5. Regras e limitações

- O SVG de terminal é uma animação ilustrativa, não executa comandos nem acessa uma máquina.
- Os badges `shields.io` ainda dependem de serviço externo, mas banners, terminal e telemetria são arquivos locais.
- O SVG de métricas exibe apenas dados públicos; pode não coincidir com o número de *contributions* do calendário do GitHub.
- Não edite métricas manualmente; o workflow as regenera.
