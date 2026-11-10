#!/usr/bin/env python3
"""Lucentia Studio – gerador do site estático. Uso: python3 build.py  (saída em ./dist)"""
import shutil, json, html, pathlib
from datetime import date

# ====== CONFIGURAÇÃO (edite aqui) ======
SITE_URL  = "https://SEU-DOMINIO.com.br"   # sem barra no final
WHATSAPP  = "5511980013438"   # só números com DDI, ex.: 5511999999999
INSTAGRAM = "https://instagram.com/lucentiastudio1"   # ex.: https://instagram.com/seuperfil
EMAIL     = "lucentia24@gmail.com"   # ex.: contato@seudominio.com.br
GA4_ID    = ""   # ex.: G-XXXXXXXXXX
# =======================================

ROOT = pathlib.Path(__file__).parent; DIST = ROOT/"dist"
E = html.escape
STAR = '<svg class="star" viewBox="0 0 100 100" aria-hidden="true"><path d="M50 0C54 36 64 46 100 50 64 54 54 64 50 100 46 64 36 54 0 50 36 46 46 36 50 0Z"/></svg>'

HL = '<img class="hl" src="/assets/logo-completo-ouro.png" alt="Lucentia Studio" width="260" height="153">'
ML = '<img class="ml" src="/assets/monograma-dourado.png" alt="" width="56" height="55" loading="lazy">'

SERVICES = [
 dict(slug="desenvolvimento-de-sites", n="01", name="Desenvolvimento de sites", short="Sites institucionais, landing pages e reformulação de sites existentes. Experiências digitais responsivas, estratégicas e alinhadas à identidade de cada negócio.",
  title="Desenvolvimento de sites institucionais e landing pages", desc="Criação de sites institucionais, landing pages e reformulação de sites com design autoral, responsivo e estruturado para buscas.",
  h1="Um site que sustenta a imagem do seu negócio.", lead="Sites institucionais, landing pages e reformulações pensados a partir da estratégia, e não de um modelo pronto.",
  about="Seu site é o lugar onde a percepção sobre o negócio se confirma ou se desfaz. Desenvolvemos cada projeto a partir do posicionamento, do público e do objetivo da empresa, com design sob medida, código limpo e estrutura preparada para ser encontrada.",
  extra_t="Qual solução faz sentido para você", extra=[("Site institucional","Para empresas que precisam apresentar quem são, o que fazem e transmitir credibilidade em várias páginas: serviços, sobre, projetos e contato."),("Landing page","Para uma ação específica: captar contatos, divulgar um serviço ou sustentar uma campanha. Uma página, um objetivo, uma chamada clara."),("Reformulação","Para quem já tem site, mas ele está desatualizado, lento, difícil de usar no celular ou não representa mais o negócio.")],
  problems=["O site atual não transmite o nível de qualidade do que a empresa oferece.","Visitantes chegam, mas não entendem a proposta ou não sabem como entrar em contato.","A navegação no celular é ruim ou o carregamento é lento."],
  benefits=["Identidade visual aplicada com consistência.","Layout responsivo, rápido e acessível.","Estrutura técnica preparada para SEO.","Caminhos claros até o contato."],
  inc=["Planejamento de estrutura e conteúdo","Design de interface sob medida","Desenvolvimento responsivo","Formulário de contato funcional","Configuração de SEO técnico e metadados","Integração com Google Analytics e Search Console","Publicação e orientação de uso"],
  faq=[("Quanto tempo leva um projeto?","Depende do escopo e da agilidade na entrega de conteúdos. Definimos o cronograma na etapa de estratégia, antes de iniciar o desenvolvimento."),("Posso atualizar o site depois?","Sim. Estruturamos o projeto para facilitar a manutenção e podemos combinar o acompanhamento contínuo."),("Vocês refazem sites que já existem?","Sim. Analisamos o que funciona, o que deve ser mantido e reconstruímos o restante com novo design e estrutura.")]),
 dict(slug="seo-e-presenca-digital", n="02", name="SEO e presença digital", short="Otimização para mecanismos de busca, SEO local e estruturação do Perfil da Empresa no Google. Mais oportunidades para que potenciais clientes encontrem o negócio.",
  title="SEO e presença digital: SEO local e Perfil da Empresa no Google", desc="Otimização para buscas, SEO local, estruturação do Perfil da Empresa no Google e monitoramento de resultados.",
  h1="Seja encontrado por quem já procura o que você faz.", lead="SEO, presença local e Perfil da Empresa no Google organizados para que seu negócio apareça com clareza e relevância.",
  about="Muitos clientes começam a decisão em uma busca. Trabalhamos para que o negócio esteja bem estruturado, coerente e relevante nos lugares onde essa busca acontece. SEO é um processo contínuo e depende de vários fatores, por isso não prometemos posições específicas.",
  extra_t="Frentes de trabalho", extra=[("SEO tradicional","Pesquisa de palavras-chave, estrutura de páginas, títulos, descrições e conteúdo alinhado ao que o público procura."),("SEO local","Para negócios que atendem uma região: presença consistente em buscas e mapas, com informações padronizadas."),("Perfil da Empresa no Google","Configuração e otimização do perfil: categorias, serviços, descrição, fotos e boas práticas de atualização."),("Estrutura técnica","Velocidade, mobile, dados estruturados, indexação e boas práticas que ajudam os buscadores a entender o site.")],
  problems=["Clientes procuram o serviço, mas encontram os concorrentes primeiro.","O Perfil da Empresa está incompleto ou desatualizado.","O site tem boa aparência, mas pouca estrutura para buscas."],
  benefits=["Informações consistentes em todos os pontos de contato.","Base técnica sólida para crescer organicamente.","Decisões apoiadas em dados de busca.","Relatórios claros de acompanhamento."],
  inc=["Diagnóstico de presença digital","Pesquisa de palavras-chave","Otimização on-page e técnica","Estruturação do Perfil da Empresa no Google","Orientação de conteúdo","Configuração de Search Console e Analytics","Monitoramento e relatórios"],
  faq=[("Vocês garantem a primeira posição no Google?","Não. Nenhum profissional sério pode garantir posições. Trabalhamos para melhorar a estrutura e a relevância e acompanhamos os resultados."),("Em quanto tempo aparecem resultados?","SEO costuma levar semanas ou meses, conforme mercado, concorrência e estado atual do site."),("SEO local serve para qualquer negócio?","É mais indicado para quem atende clientes em uma região específica ou possui ponto físico.")]),
 dict(slug="crm-personalizado", n="03", name="Organização comercial e CRM", short="Desenvolvimento de CRMs personalizados para organizar contatos, oportunidades e processos comerciais, reduzindo a dispersão das informações.",
  title="CRM personalizado para organização comercial", desc="Desenvolvimento de CRM sob medida para organizar contatos, leads e oportunidades de acordo com o processo comercial de cada empresa.",
  h1="Cada contato no lugar certo, cada oportunidade à vista.", lead="Um CRM simples, desenhado a partir do processo comercial da sua empresa e não o contrário.",
  about="Planilhas, mensagens e anotações espalhadas fazem oportunidades se perderem. Desenvolvemos um sistema próprio, enxuto e adaptado ao seu jeito de vender, para concentrar contatos, histórico e próximos passos em um só lugar.",
  extra_t="Como um CRM organiza sua operação", extra=[("Contatos","Cadastro centralizado com origem, histórico de conversas e dados importantes."),("Leads e oportunidades","Funil visual com etapas definidas por você, do primeiro contato ao fechamento."),("Rotina comercial","Tarefas, lembretes e retornos para que nenhuma conversa fique sem resposta.")],
  problems=["Informações de clientes espalhadas entre planilhas, WhatsApp e cadernos.","Dificuldade em saber em que etapa cada oportunidade está.","Retornos esquecidos e processo dependente de uma única pessoa."],
  benefits=["Simplicidade de uso no dia a dia.","Etapas e campos adaptados ao seu processo.","Visão clara do funil comercial.","Base para crescer com organização."],
  inc=["Mapeamento do processo comercial","Definição de campos, etapas e permissões","Desenvolvimento do sistema","Importação de contatos existentes","Treinamento de uso","Suporte inicial pós-entrega"],
  faq=[("Por que não usar um CRM pronto?","Ferramentas prontas podem atender bem. Um CRM sob medida faz sentido quando seu processo tem particularidades ou quando você quer só o que realmente usa."),("O sistema funciona no celular?","Sim, a interface é pensada para uso em desktop e dispositivos móveis."),("Meus dados ficam seguros?","Aplicamos boas práticas de segurança e definimos acessos por perfil. Os detalhes são alinhados no projeto.")]),
 dict(slug="trafego-pago", n="04", name="Tráfego pago", short="Planejamento e gestão de campanhas no Google Ads e Meta Ads para ampliar o alcance e atrair potenciais clientes.",
  title="Tráfego pago: gestão de Google Ads e Meta Ads", desc="Planejamento e gestão de campanhas no Google Ads e Meta Ads, com segmentação, páginas de destino e acompanhamento.",
  h1="Alcance as pessoas certas, no momento certo.", lead="Campanhas no Google Ads e Meta Ads planejadas com estratégia, segmentação e acompanhamento constante.",
  about="Anúncios funcionam melhor quando há clareza sobre público, oferta e destino do clique. Planejamos e gerenciamos as campanhas e cuidamos da página de destino para que o investimento leve a contatos reais. O valor investido em mídia é pago diretamente às plataformas e é separado do serviço de gestão.",
  extra_t="Plataformas", extra=[("Google Ads","Alcance pessoas no momento em que buscam por um serviço ou produto, em pesquisa, mapas e outras redes."),("Meta Ads","Anúncios no Instagram e Facebook, com segmentação por interesses, comportamento e região, ideais para gerar reconhecimento e contatos.")],
  problems=["Anúncios ativos, mas sem clareza sobre o que gera contatos.","Cliques que não se convertem por falta de página de destino adequada.","Investimento sem segmentação ou acompanhamento."],
  benefits=["Campanhas alinhadas a objetivos definidos.","Segmentação cuidadosa do público.","Páginas de destino pensadas para conversão.","Acompanhamento e ajustes contínuos."],
  inc=["Planejamento e estrutura das campanhas","Definição de públicos e segmentações","Criação de anúncios e textos","Configuração de rastreamento e conversões","Recomendações para páginas de destino","Relatórios periódicos e otimizações"],
  faq=[("O investimento em anúncios está incluso?","Não. A verba de mídia é paga diretamente ao Google ou à Meta. O nosso serviço é o planejamento e a gestão."),("Quanto preciso investir?","Depende do mercado, da região e dos objetivos. Definimos uma faixa realista no planejamento."),("Vocês prometem número de clientes?","Não. Resultados variam por mercado e oferta. Acompanhamos e otimizamos com base em dados.")]),
]
STEPS=[("Imersão","Entender o negócio, seus objetivos e desafios."),("Estratégia","Definir posicionamento, estrutura e soluções."),("Desenvolvimento","Transformar a estratégia em uma experiência digital."),("Evolução","Acompanhar, analisar e aprimorar quando contratado.")]
# Para adicionar projetos: acrescente um item. kind: "conceitual" ou "real". url vazio = sem link ainda.
PROJECTS=[
 dict(slug="still-point-tattoo",name="Still Point Tattoo",seg="Estúdio de tatuagem",cat="Site institucional",kind="real",url="https://stillpointtattoo.netlify.app/",cover="/assets/projetos/capa-still-point.webp",
  desc="Site institucional para um estúdio de tatuagem em Santo André (SP), com apresentação do estúdio, tatuadores, trabalhos e contato direto por WhatsApp.",sol="Site institucional com formulário integrado ao WhatsApp",
  about="O Still Point Tattoo é um estúdio privado em Santo André, SP. O site apresenta o conceito do estúdio, o time de tatuadores residentes, uma amostra dos trabalhos de cada profissional e um caminho direto para marcar horário. O formulário reúne nome, WhatsApp, ideia da tatuagem e região do corpo, e continua a conversa no WhatsApp, com consentimento de uso dos dados (LGPD).",
  feats=["Identidade visual própria, com o símbolo do estúdio em destaque","Página do time, com perfil e portfólio de cada tatuador","Galeria de trabalhos","Formulário que continua a conversa no WhatsApp","Consentimento de uso de dados (LGPD)","Botão de agendamento sempre visível no menu"],
  shots=[("/assets/projetos/still-point-home.webp","Página inicial",1400,637),("/assets/projetos/still-point-tatuadores.webp","Tatuadores",1400,636),("/assets/projetos/still-point-trabalhos.webp","Trabalhos",1400,622),("/assets/projetos/still-point-contato.webp","Contato e formulário",1400,630)]),
 dict(slug="crm-still-point",name="CRM Still Point",seg="Estúdio de tatuagem",cat="CRM personalizado",kind="real",url="",nolink="Sistema de acesso restrito",cover="/assets/projetos/capa-crm-still-point.webp",
  desc="CRM sob medida para organizar leads, agenda e clientes de um estúdio de tatuagem, com funil de atendimento do primeiro contato ao serviço concluído.",sol="CRM personalizado com funil, agenda e clientes",
  about="Um sistema de uso interno desenvolvido para a rotina do estúdio. Reúne os contatos em um funil com etapas próprias (Novo, Conversando, Orçamento, Sinal pago, Agendado, Feito e Perdido), mostra os próximos atendimentos, lembra as mensagens que precisam ser enviadas e traz um resumo do período. A área exige login, por isso a imagem mostra apenas a tela de resumo, sem dados de clientes.",
  feats=["Funil com sete etapas de atendimento","Agenda de atendimentos","Cadastro de clientes","Lista de mensagens a enviar no dia","Resumo com leads, agendamentos e conversão","Área com login"],
  shots=[("/assets/projetos/crm-still-point-resumo.webp","Tela de resumo",1400,404)]),
 dict(name="Aurora Clínica",seg="Saúde e bem-estar",cat="Site institucional",kind="conceitual",url="",desc="Conceito de site institucional para clínica, com foco em acolhimento, clareza de serviços e agendamento.",sol="Site de 5 páginas, SEO local e formulário",art=1),
 dict(name="Atelier Norte",seg="Arquitetura e interiores",cat="Landing page",kind="conceitual",url="",desc="Conceito de landing page para escritório de arquitetura, com portfólio em destaque e contato direto.",sol="Landing page e página de destino para anúncios",art=2),
 dict(name="Casa Meridiana",seg="Gastronomia",cat="Reformulação",kind="conceitual",url="",desc="Conceito de reformulação para restaurante, com cardápio, reservas e presença no Google.",sol="Redesign, Perfil da Empresa no Google",art=3)]

def art(i):
    a={1:'<circle cx="260" cy="250" r="150" fill="none" stroke="#E4C78A" stroke-width="1.5"/><circle cx="340" cy="250" r="150" fill="none" stroke="#E4C78A" stroke-width="1.5" opacity=".5"/>',
       2:'<path d="M80 420V120h60M80 420h300" fill="none" stroke="#17352F" stroke-width="22"/><path d="M360 90C366 150 380 164 430 170 380 176 366 190 360 250 354 190 340 176 290 170 340 164 354 150 360 90Z" fill="#17352F"/>',
       3:''.join(f'<line x1="{60+k*40}" y1="460" x2="{60+k*40}" y2="{300-k*22}" stroke="#E4C78A" stroke-width="2"/>' for k in range(10))}[i]
    bg={1:"#17352F",2:"#E4C78A",3:"#0f2420"}[i]
    return f'<svg viewBox="0 0 560 500" role="img" aria-label="Capa ilustrativa do projeto conceitual" preserveAspectRatio="xMidYMid slice"><rect width="560" height="500" fill="{bg}"/>{a}</svg>'

def link_wa(t="Fale no WhatsApp"):
    return f'<a class="tl" href="https://wa.me/{WHATSAPP}" rel="noopener" target="_blank">{t}</a>' if WHATSAPP else ""

def page(path,title,desc,body,schema=None,noindex=False):
    url=SITE_URL+path
    nav=''.join(f'<a href="{h}"{" aria-current=page" if h==path else ""}>{t}</a>' for h,t in [("/servicos/desenvolvimento-de-sites/","Serviços"),("/projetos/","Projetos"),("/#metodo","Método"),("/#sobre","Sobre"),("/contato/","Contato")])
    ga=f'<script async src="https://www.googletagmanager.com/gtag/js?id={GA4_ID}"></script><script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag("js",new Date());gtag("config","{GA4_ID}")</script>' if GA4_ID else ""
    ld=json.dumps({"@context":"https://schema.org","@type":"Organization","name":"Lucentia Studio","url":SITE_URL,"logo":SITE_URL+"/assets/logo-completo-ouro.png","description":"Estúdio de soluções digitais: sites, SEO, CRM e tráfego pago.",**({"sameAs":[INSTAGRAM]} if INSTAGRAM else {})},ensure_ascii=False)
    sv=''.join(f'<li><a href="/servicos/{s["slug"]}/">{s["name"]}</a></li>' for s in SERVICES)
    soc=''.join(f'<li><a href="{h}" rel="noopener" target="_blank">{t}</a></li>' for h,t in [(INSTAGRAM,"Instagram"),(f"https://wa.me/{WHATSAPP}" if WHATSAPP else "","WhatsApp"),(f"mailto:{EMAIL}" if EMAIL else "",EMAIL)] if h)
    return f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title><meta name="description" content="{E(desc)}"><link rel="canonical" href="{url}">{'<meta name="robots" content="noindex">' if noindex else ''}
<meta name="theme-color" content="#17352F"><meta property="og:type" content="website"><meta property="og:locale" content="pt_BR"><meta property="og:site_name" content="Lucentia Studio"><meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="{SITE_URL}/assets/og.png"><meta name="twitter:card" content="summary_large_image">
<link rel="icon" type="image/png" href="/assets/monograma-dourado.png"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Raleway:wght@400;500;600&family=Red+Hat+Display:wght@400;500;700&display=swap"><link rel="stylesheet" href="/assets/style.css">
<script type="application/ld+json">{ld}</script>{ga}</head><body>
<a class="skip" href="#main">Ir para o conteúdo</a>
<header class="hd"><a class="logo" href="/" aria-label="Lucentia Studio, página inicial"><img src="/assets/monograma-dourado.png" alt="Lucentia Studio" width="47" height="46"></a>
<button class="mt" aria-expanded="false" aria-controls="nav">Menu</button><nav id="nav" aria-label="Principal">{nav}</nav></header>
<main id="main">{body}</main>
<footer class="ft dark"><div class="wrap fg"><div><img class="flogo" src="/assets/logo-completo-ouro.png" alt="Lucentia Studio" width="220" height="130" loading="lazy"><p class="sm">Estúdio de soluções digitais.</p></div>
<nav aria-label="Rodapé"><h2 class="fh">Navegação</h2><ul><li><a href="/">Início</a></li><li><a href="/projetos/">Projetos</a></li><li><a href="/#metodo">Método</a></li><li><a href="/contato/">Contato</a></li></ul></nav>
<div><h2 class="fh">Serviços</h2><ul>{sv}</ul></div><div><h2 class="fh">Contato</h2><ul><li><a href="/contato/">Formulário</a></li>{soc}</ul></div></div>
<div class="wrap cp sm">© {date.today().year} Lucentia Studio. Todos os direitos reservados.</div></footer><script src="/assets/main.js" defer></script></body></html>'''

def cta(t="Seu próximo passo começa com uma boa ideia.",p="Vamos conversar sobre o que podemos construir para o seu negócio.",b="Fale com a Lucentia"):
    return f'<section class="dark cta"><div class="wrap">{ML}<h2 class="big">{t}</h2><p class="lead">{p}</p><a class="btn" href="/contato/">{b}</a>{link_wa()}</div></section>'

def proj_card(p):
    conc=p["kind"]=="conceitual"; tag="Projeto conceitual" if conc else "Projeto"
    cover=f'<img src="{p["cover"]}" alt="Capa do projeto {E(p["name"])}" width="700" height="500" loading="lazy">' if p.get("cover") else art(p["art"])
    lk=[]
    if p.get("slug"): lk.append(f'<a class="tl" href="/projetos/{p["slug"]}/">Ver projeto<span class="sr"> {E(p["name"])}</span></a>')
    if p.get("url"): lk.append(f'<a class="tl" href="{p["url"]}" rel="noopener" target="_blank">Visitar site<span class="sr"> {E(p["name"])}</span></a>')
    elif p.get("nolink"): lk.append(f'<span class="sm mut">{p["nolink"]}</span>')
    if not lk: lk.append('<span class="sm mut">Prévia em breve</span>')
    return f'''<article class="pc" data-kind="{p["kind"]}"><div class="pi">{cover}</div><div class="pm"><span class="tag {p["kind"]}">{tag}</span><h3>{p["name"]}</h3><p class="sm mut">{p["seg"]} · {p["cat"]}</p><p>{p["desc"]}</p><p class="sm"><strong>Solução:</strong> {p["sol"]}</p><div class="lk">{"".join(lk)}</div></div></article>'''

def home():
    rows=''.join(f'<a class="sr-row" href="/servicos/{s["slug"]}/"><span class="n">{s["n"]}</span><h3>{s["name"]}</h3><p>{s["short"]}</p>{STAR}</a>' for s in SERVICES)
    st=''.join(f'<li><span class="n">0{i+1}</span><h3>{a}</h3><p>{b}</p></li>' for i,(a,b) in enumerate(STEPS))
    return f'''<section class="hero dark"><div class="glow" aria-hidden="true"></div><div class="heroart" aria-hidden="true">{STAR}</div><div class="wrap">{HL}<h1>Mais visibilidade.<br>Mais oportunidades.</h1>
<p class="lead">Desenvolvemos experiências digitais que fortalecem marcas, ampliam sua presença e transformam oportunidades em crescimento.</p>
<p class="acts"><a class="btn" href="/contato/">Vamos conversar</a><a class="tl" href="/projetos/">Conheça nosso trabalho</a></p></div></section>
<section class="light pad" id="apresentacao"><div class="wrap two"><h2 class="big">Presença digital com intenção.</h2><p class="lead">Cada negócio tem uma história, uma identidade e objetivos próprios. Nosso trabalho é transformar esses elementos em experiências digitais que comunicam com clareza, fortalecem a percepção da marca e aproximam empresas de novas oportunidades.</p></div></section>
<section class="light pad nt" id="servicos"><div class="wrap"><h2 class="sec">Serviços</h2><div class="rows">{rows}</div></div></section>
<section class="dark pad" id="projetos"><div class="wrap"><div class="sh"><h2 class="big">Projetos</h2><a class="tl" href="/projetos/">Ver todos os projetos</a></div><div class="pg">{''.join(proj_card(p) for p in PROJECTS[:3])}</div><p class="sm mut note">Projetos identificados como conceituais são criados para demonstrar nossa abordagem e não representam clientes reais nem resultados comerciais.</p></div></section>
<section class="light pad" id="metodo"><div class="wrap"><h2 class="big">Pensamento estratégico.<br>Execução precisa.</h2><ol class="steps">{st}</ol></div></section>
<section class="green pad" id="sobre"><div class="wrap two"><h2 class="big">Mais do que presença. Uma forma de se destacar.</h2><div class="lead"><p>A Lucentia Studio nasceu da ideia de que a presença digital de um negócio deve refletir a qualidade do que ele oferece.</p><p>Unimos estratégia, design e tecnologia para desenvolver soluções digitais que fazem sentido para cada empresa.</p><p>Acreditamos que bons projetos começam com boas perguntas, decisões inteligentes e atenção aos detalhes.</p></div></div><div class="wrap seal"><img class="biglogo" src="/assets/logo-completo-ouro.png" alt="Lucentia Studio" width="320" height="188" loading="lazy"></div></section>{cta()}'''

def service(s):
    L=lambda a:''.join(f'<li>{x}</li>' for x in a)
    ex=''.join(f'<div class="ex"><h3>{a}</h3><p>{b}</p></div>' for a,b in s["extra"])
    stp=''.join(f'<li><span class="n">0{i+1}</span><h3>{a}</h3><p>{b}</p></li>' for i,(a,b) in enumerate(STEPS[:3]+[("Entrega","Publicação, orientação de uso e definição dos próximos passos.")] ))
    fq=''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q,a in s["faq"])
    return f'''<section class="hero dark sub"><div class="heroart" aria-hidden="true">{STAR}</div><div class="wrap">{HL}<p class="sm gold">{s["n"]} · {s["name"]}</p><h1>{s["h1"]}</h1><p class="lead">{s["lead"]}</p><p class="acts"><a class="btn" href="/contato/?servico={s["slug"]}">Solicitar conversa</a></p></div></section>
<section class="light pad"><div class="wrap two"><h2 class="big">O serviço</h2><p class="lead">{s["about"]}</p></div></section>
<section class="light pad nt"><div class="wrap"><h2 class="sec">{s["extra_t"]}</h2><div class="exg">{ex}</div></div></section>
<section class="green pad"><div class="wrap two"><div><h2 class="sec">Problemas que resolve</h2><ul class="ls">{L(s["problems"])}</ul></div><div><h2 class="sec">Benefícios</h2><ul class="ls">{L(s["benefits"])}</ul></div></div></section>
<section class="light pad"><div class="wrap two"><h2 class="big">O que está incluído</h2><ul class="ls dk">{L(s["inc"])}</ul></div></section>
<section class="light pad nt"><div class="wrap"><h2 class="sec">Como funciona o desenvolvimento</h2><ol class="steps">{stp}</ol></div></section>
<section class="light pad nt"><div class="wrap two"><h2 class="big">Perguntas frequentes</h2><div class="faq">{fq}</div></div></section>{cta("Vamos conversar sobre "+s["name"].lower()+".","Conte o que você precisa e indicamos o melhor caminho.","Fale com a Lucentia")}'''

def projetos():
    return f'''<section class="hero dark sub"><div class="wrap">{HL}<h1>Projetos</h1><p class="lead">Trabalhos conceituais e reais, identificados com clareza.</p></div></section>
<section class="light pad"><div class="wrap"><div class="flt" role="group" aria-label="Filtrar projetos"><button aria-pressed="true" data-f="todos">Todos</button><button aria-pressed="false" data-f="conceitual">Conceituais</button><button aria-pressed="false" data-f="real">Projetos</button></div>
<div class="pg lt">{''.join(proj_card(p) for p in PROJECTS)}</div><p class="empty sm" hidden>Ainda não há projetos nesta categoria.</p>
<p class="sm mut note">Projetos conceituais são criados pela Lucentia para demonstrar abordagem e não representam clientes reais ou resultados comerciais.</p></div></section>{cta()}'''

def contato():
    opts=''.join(f'<option value="{s["slug"]}">{s["name"]}</option>' for s in SERVICES)+'<option value="outro">Outro / ainda não sei</option>'
    side=''.join(x for x in [link_wa(), f'<a class="tl" href="{INSTAGRAM}" rel="noopener" target="_blank">Instagram</a>' if INSTAGRAM else "", f'<a class="tl" href="mailto:{EMAIL}">{EMAIL}</a>' if EMAIL else ""])
    return f'''<section class="hero dark sub"><div class="wrap">{HL}<h1>Vamos conversar sobre seu próximo projeto.</h1><p class="lead">Conte um pouco sobre seu negócio e o que gostaria de desenvolver. Vamos entender suas necessidades e pensar na melhor solução.</p></div></section>
<section class="light pad"><div class="wrap two"><form class="fm" name="contato" method="POST" action="/obrigado/" data-netlify="true" netlify-honeypot="bot-field"><input type="hidden" name="form-name" value="contato"><p class="hp"><label>Não preencha <input name="bot-field"></label></p>
<label>Nome<input name="nome" required autocomplete="name"></label><label>Empresa<input name="empresa" autocomplete="organization"></label><label>E-mail<input type="email" name="email" required autocomplete="email"></label><label>WhatsApp<input type="tel" name="whatsapp" autocomplete="tel" placeholder="(DDD) 00000-0000"></label>
<label>Serviço de interesse<select name="servico">{opts}</select></label><label>Mensagem<textarea name="mensagem" rows="5" required></textarea></label><button class="btn" type="submit">Enviar mensagem</button><p class="st sm" role="status" aria-live="polite"></p></form>
<aside class="side"><h2 class="sec">Outros canais</h2>{side or '<p class="sm mut">Use o formulário e retornaremos em breve.</p>'}<img class="biglogo sd" src="/assets/logo-completo-verde.png" alt="Lucentia Studio" width="220" height="130" loading="lazy"></aside></div></section>'''

def project_page(p):
    shots="".join(f'<figure class="shot{" full" if i==0 else ""}"><img src="{src}" alt="{E(cap)} do projeto {E(p["name"])}" width="{w}" height="{h}" loading="lazy"><figcaption>{E(cap)}</figcaption></figure>' for i,(src,cap,w,h) in enumerate(p["shots"]))
    visit=f'<a class="btn" href="{p["url"]}" rel="noopener" target="_blank">Visitar o site</a>' if p.get("url") else f'<span class="sm gold">{p.get("nolink","")}</span>'
    ft="".join(f"<li>{x}</li>" for x in p["feats"])
    meta="".join(f"<div><dt>{k}</dt><dd>{E(v)}</dd></div>" for k,v in [("Segmento",p["seg"]),("Categoria",p["cat"]),("Solução",p["sol"])])
    return f'''<section class="hero dark sub"><div class="wrap">{HL}<p class="sm gold">{E(p["seg"])} · {E(p["cat"])}</p><h1>{E(p["name"])}</h1><p class="lead">{E(p["desc"])}</p><p class="acts">{visit}<a class="tl" href="/projetos/">Todos os projetos</a></p></div></section>
<section class="light pad"><div class="wrap two"><h2 class="big">Sobre o projeto</h2><div><p class="lead">{E(p["about"])}</p><dl class="meta">{meta}</dl></div></div></section>
<section class="green pad"><div class="wrap two"><h2 class="big">O que foi desenvolvido</h2><ul class="ls">{ft}</ul></div></section>
<section class="light pad"><div class="wrap"><h2 class="sec">Imagens do projeto</h2><div class="shots">{shots}</div></div></section>{cta("Quer um projeto como este?","Conte sobre o seu negócio e vamos pensar na melhor solução.")}'''

def write(p,c):
    f=DIST/p.strip("/")/"index.html" if p!="/404.html" else DIST/"404.html"; f.parent.mkdir(parents=True,exist_ok=True); f.write_text(c,encoding="utf-8")

shutil.rmtree(DIST,ignore_errors=True); DIST.mkdir(); shutil.copytree(ROOT/"assets",DIST/"assets")
urls=["/","/projetos/","/contato/"]
write("/",page("/","Lucentia Studio | Estúdio de soluções digitais","Sites, SEO, CRM e tráfego pago com estratégia e design autoral. Mais visibilidade e mais oportunidades para o seu negócio.",home()))
for s in SERVICES:
    p=f'/servicos/{s["slug"]}/'; urls.append(p); write(p,page(p,s["title"]+" | Lucentia Studio",s["desc"],service(s)))
write("/projetos/",page("/projetos/","Projetos | Lucentia Studio","Projetos conceituais e reais desenvolvidos pela Lucentia Studio: sites, landing pages e reformulações.",projetos()))
for p_ in PROJECTS:
    if p_.get("slug"):
        u=f'/projetos/{p_["slug"]}/'; urls.append(u); write(u,page(u,f'{p_["name"]}: {p_["cat"]} | Lucentia Studio',p_["desc"],project_page(p_)))
write("/contato/",page("/contato/","Contato | Lucentia Studio","Conte sobre seu negócio e o que gostaria de desenvolver. Fale com a Lucentia Studio.",contato()))
write("/obrigado/",page("/obrigado/","Mensagem enviada | Lucentia Studio","Recebemos sua mensagem.",'<section class="hero dark sub"><div class="wrap"><img class="biglogo" src="/assets/logo-completo-ouro.png" alt="Lucentia Studio" width="200" height="118"><h1>Mensagem enviada.</h1><p class="lead">Obrigado pelo contato. Retornaremos em breve.</p><p class="acts"><a class="btn" href="/">Voltar ao início</a></p></div></section>',noindex=True))
write("/404.html",page("/404.html","Página não encontrada | Lucentia Studio","Página não encontrada.",'<section class="hero dark sub"><div class="wrap">'+HL+'<h1>Página não encontrada.</h1><p class="lead">O endereço pode ter mudado. Volte ao início ou veja nossos serviços.</p><p class="acts"><a class="btn" href="/">Voltar ao início</a></p></div></section>',noindex=True))
(DIST/"sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join(f'<url><loc>{SITE_URL}{u}</loc></url>' for u in urls)+'</urlset>')
(DIST/"robots.txt").write_text(f"User-agent: *\nAllow: /\nDisallow: /obrigado/\n\nSitemap: {SITE_URL}/sitemap.xml\n")
print("OK:",len(urls),"páginas")
