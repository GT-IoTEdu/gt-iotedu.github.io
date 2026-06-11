# Revisão de Paper — SBSeg 2026
**Título:** Uma Abordagem Multiagente para Geração e Validação de Regras Snort em Cenários IoT
**Nível de rigor aplicado:** USENIX Security / NDSS / SIGCOMM
**Data da revisão:** 2026-05-22

---

## CRITÉRIO 1 — ANONIMIDADE [pré-condição]

### ⚠ FALHA DE ANONIMIDADE DETECTADA

**Ocorrência:** Rodapé 2 da Seção 4 (página 4), parágrafo de apresentação da arquitetura:

> `https://github.com/cwrricio/ataques-sbseg26`

**Análise da violação:**

- **Username GitHub identificável:** O segmento `cwrricio` é um username de conta pública no GitHub. Qualquer revisor que acesse o link pode visualizar o perfil da conta, listar os repositórios públicos e, a partir dos commits/contribuidores do repositório, identificar os autores do paper. Mesmo que a conta seja pseudônima, ela constitui um artefato externo potencialmente rastreável.
- **Nome do repositório revela a venue:** `ataques-sbseg26` menciona explicitamente "sbseg26", o que confirma tratar-se de artefato associado a esta submissão ao SBSeg 2026, reduzindo ainda mais o espaço de anonimato.
- **Impacto:** Em revisão duplamente cega com padrão USENIX Security/NDSS, a exposição de um repositório vinculado a uma identidade (ainda que pseudônima e pública) constitui violação do processo de anonimização. O revisor que acessar o link antes de avaliar o paper terá informações de autoria que podem influenciar o julgamento, comprometendo a integridade do processo.

**Demais elementos verificados:**
- Identificação dos autores na folha de rosto: "Autoria Anônima / Instituição Anônima" — correto.
- Rodapé 1 com URL pública do Snort Community Rules (snort.org) — não identificador, aceitável.
- Auto-citações: não foram identificadas auto-citações em primeira ou terceira pessoa que tornem a autoria identificável de forma direta.
- Metadados de PDF: não verificáveis nesta avaliação.

**Nota: 1/5 — FALHA**
Per os critérios desta revisão, a falha de anonimidade implica **rejeição direta**. Os demais critérios são avaliados na íntegra para subsidiar a resubmissão.

---

## CRITÉRIO 2 — INTRODUÇÃO

### 2a. Contextualização do problema com dados técnicos e concretos — **3/5**

A introdução apresenta um dado concreto relevante: "nenhuma regra comunitária disparou alerta contra os sete cenários IoT avaliados" — este é o ponto empírico central que justifica a pesquisa. Contudo, a contextualização carece de métricas externas que quantifiquem a magnitude do problema em campo real:

- Não são apresentadas taxas de ataque IoT em ambientes de produção (e.g., crescimento de incidentes envolvendo MQTT/XRCE-DDS em relatórios como ENISA Threat Landscape ou Cisco Talos).
- Não há dados sobre o custo médio de um incidente em ambientes industriais/ciberfísicos com IDS ineficaz.
- A afirmação "assinaturas da comunidade Snort concentram-se historicamente em servidores web e sistemas legados" é essencialmente qualitativa; um dado quantitativo (e.g., percentual das regras comunitárias classificadas por protocolo) fortaleceria o argumento.

O problema é inteligível e motivado, mas a "dor" não é quantificada com a precisão esperada em tier-1.

### 2b. Parágrafo de limitações dos trabalhos relacionados — **3/5**

Existe um parágrafo dedicado às limitações, com o seguinte argumento central: abordagens com LLM "permanecem limitadas a validações estáticas ou textuais, deixando invisíveis regras excessivamente específicas que falham diante de mutações triviais do vetor ofensivo." Este argumento é tecnicamente correto e representa a contribuição diferencial do trabalho.

Pontos fracos:
- A limitação é enunciada de forma genérica para a maioria dos trabalhos, sem citar falhas concretas e documentadas (e.g., "o sistema X de [referência] gerou regra que foi evasiva com simples variação de TTL, conforme demonstrado em [referência]").
- A correspondência entre as limitações apontadas e as contribuições do paper é implícita, não explicitada estruturalmente.

### 2c. Clareza e completude das contribuições — **3/5**

As quatro contribuições são enumeradas (i–iv) e mapeiam para seções identificáveis do paper. Contudo:

- Nenhuma contribuição possui métrica verificável a priori: não há afirmação do tipo "atingimos IC médio de X iterações e TDV de Y%" ou "reduzimos falsos negativos em Z% em relação à linha de base".
- A contribuição (i) — confirmação experimental da lacuna — é uma validação de hipótese já razoavelmente estabelecida na comunidade, não uma contribuição técnica nova por si só.
- As contribuições (iii) e (iv) são parcialmente redundantes na formulação apresentada.

### 2d. Fluidez e objetividade — **4/5**

A introdução é concisa (aproximadamente duas páginas), sem redundâncias significativas. A sequência problema → lacuna → proposta → contribuições é clara e linear. Aprovado.

**Nota Consolidada Critério 2: 3/5**

---

## CRITÉRIO 3 — TRABALHOS RELACIONADOS E TABELA COMPARATIVA [peso 2x]

### 3a. Existência e qualidade da tabela comparativa — **2/5**

A Tabela 1 existe. Contudo, apresenta deficiências estruturais graves para o padrão tier-1:

**Colunas presentes:**
| Coluna | Avaliação |
|---|---|
| Referência | Obrigatória, adequada |
| Abordagem | Descritiva, não padronizada. Não permite comparação estruturada |
| Usa LLMs | **Trivial e inadequada.** 8 de 10 entradas são "Sim"; a coluna não discrimina nada relevante no contexto de 2025–2026, onde LLMs são ubíquos. Deve ser removida |
| Tipo de Validação | Tecnicamente relevante e discriminativa — é a coluna central do argumento |

**Colunas ausentes que seriam essenciais:**

- **Protocolo/domínio alvo** (network-generic, HTTP/web, MQTT, SCADA, etc.) — crítico para situar a contribuição IoT.
- **Modelo de ameaça** (adversário passivo/ativo, capacidade de mutação do vetor ofensivo) — central para comparar robustez.
- **Avaliação de falsos positivos** (sim/não/não relatado) — métrica fundamental de qualidade de assinatura.
- **Disponibilidade de artefatos** (código/dataset público, sim/não) — relevante para reprodutibilidade.
- **Escala de avaliação** (número de regras geradas, número de cenários/protocolos) — permite comparar abrangência.
- **Custo computacional / latência de síntese** — relevante para operacionalização.

A tabela, em seu estado atual, funciona apenas como bibliografia anotada com uma classificação binária. Ela não permite ao leitor entender *por que* a proposta avança sobre o estado da arte de forma estruturada.

### 3b. Estrutura da discussão — **3/5**

A seção organiza os trabalhos por grupo tecnológico (algoritmos genéticos → LLMs offline → loops de feedback), o que é correto metodologicamente. A narrativa conecta as limitações de cada grupo às contribuições do paper.

Fragilidades:
- A discussão dos grupos é excessivamente breve (3–4 parágrafos para 10 trabalhos), com pouca profundidade técnica por grupo.
- Não há análise de falhas concretas e verificáveis nos trabalhos relacionados; apenas classificações de alto nível.
- A distinção entre "validação reativa" (GRIDAI) e "validação dinâmica proativa" (proposta) poderia ser mais articulada tecnicamente.

### 3c. Cobertura e atualidade — **4/5**

A cobertura dos trabalhos recentes é sólida, incluindo referências de 2025–2026 (RulePilot, GRIDAI, RuleMaster+, FALCON, UniRule). A dimensão temporal é adequada. Há uma lacuna notável: nenhum trabalho sobre detecção de intrusão específica para IoT *sem* LLMs (e.g., abordagens baseadas em anomalia de comportamento de protocolo MQTT) é citado como baseline alternativo, o que estreita a perspectiva comparativa.

**Nota Consolidada Critério 3: 2/5**

---

## CRITÉRIO 4 — METODOLOGIA E DESIGN TÉCNICO

### 4a. Clareza e corretude do modelo de ameaça — **2/5**

O paper **não apresenta um modelo de ameaça explícito e formalizado**. As capacidades do adversário são operacionalizadas implicitamente através da descrição do Agente de Ataque, mas sem definição formal:

- Não é declarado o que o adversário conhece (black-box, grey-box, white-box em relação ao IDS?).
- Não são definidas as capacidades de rede do adversário (acesso à mesma sub-rede? capacidade de spoofing?).
- O adversário emulado tem acesso a catálogos de técnicas de evasão documentadas publicamente — isso é um grey-box assumption que não é explicitado como tal.
- A ausência de um threat model formal é uma lacuna séria para um paper de segurança tier-1, onde a seção de threat model é obrigatória.

### 4b. Rigor técnico do design proposto — **3/5**

O design é bem articulado e internamente consistente. Os quatro passos do Agente de Defesa (enriquecimento → síntese → validação sintática → implantação) e os sete ferramentais do Agente de Ataque são descritos com clareza suficiente para compreensão arquitetural.

Pontos cegos identificados:
- O critério de convergência (20 detecções consecutivas) é heurístico e **não justificado teoricamente**. Por que 20? Qual a relação com a distribuição esperada de variantes de um ataque real?
- O processo de "enriquecimento de contexto" pelo Agente de Defesa (Seção 4.1) — que expande o prompt inicial com vetores de ameaça — não é detalhado. Os prompts usados não são divulgados, o que impede avaliação do impacto do prompt engineering nos resultados.
- O mecanismo de "persistência de regras validadas" (biblioteca de regras por tipo de ataque) não tem sua estratégia de recuperação especificada: as regras são recuperadas por similaridade semântica? Por hash? Isso é relevante para reproduzir o comportamento do sistema.

### 4c. Reprodutibilidade — **3/5**

O repositório público é referenciado (mas viola anonimato). Os parâmetros principais estão declarados: DeepSeek V4 Pro, temperatura zero, framework Agno. O testbed de duas máquinas é descrito.

Lacunas de reprodutibilidade:
- Templates de prompts (system prompts dos agentes) não são fornecidos no paper.
- O formato exato dos "catálogos de família de ataque" (sete documentos de referência) não está descrito estruturalmente.
- O processo de "lógica de decisão do Orquestrador" não tem pseudocódigo ou fluxograma detalhado além da Figura 1.

**Nota Consolidada Critério 4: 3/5**

---

## CRITÉRIO 5 — AVALIAÇÃO E RESULTADOS

### 5a. Solidez e coerência dos resultados — **3/5**

Os resultados são coerentes internamente: IC crescente para ataques mais complexos (MQTT QoS IC=1 vs Fragment Abuse IC=10) é plausível e bem explicado. O não-convergência do Entity Flood é reportado honestamente. As métricas TDV e TE são complementares e fornecem visão bidimensional da robustez.

Fragilidades:
- Não há comparação direta com um baseline competidor: "o que aconteceria se um engenheiro humano escrevesse as regras?" ou "o que aconteceria com RulePilot/GRIDAI nos mesmos cenários?". A única comparação é a bateria de controle (100% de detecção sem variantes adversariais), que é trivial e não constitui um baseline técnico justo.
- A afirmação de que "todos os cenários tiveram taxa de evasão final abaixo de 50%" é apresentada como evidência de sucesso, mas sem referencial normativo: o que seria uma taxa de evasão aceitável em produção?

### 5b. Rigor experimental — **2/5**

Esta é a fraqueza experimental mais crítica do paper:

- **Ausência total de intervalos de confiança ou análise de significância estatística.** Com 297 execuções distribuídas em 7 cenários (média de ~42 execuções/cenário), os resultados são apresentados como valores pontuais sem variância.
- **Avaliação com modelo único** (DeepSeek V4 Pro, temperatura 0). Não há ablação de modelos nem de configurações de temperatura. O comportamento do sistema com outro LLM (e.g., GPT-4o, Claude Sonnet) é completamente desconhecido.
- **Ausência de avaliação de falsos positivos.** O paper menciona que "tráfego benigno foi utilizado para evitar a identificação de falsos positivos" (Seção 4.2), mas nenhum resultado sobre a taxa de FP das regras geradas é reportado. Para uma assinatura de IDS, a relação precisão/revocação é fundamental — apresentar apenas recall sem precisão é uma omissão grave.
- **Uma única execução por configuração.** Dada a natureza estocástica dos LLMs (mesmo a temperatura 0 não garante determinismo completo em todos os provedores), idealmente haveria múltiplas execuções independentes por cenário.

### 5c. Ameaças à validade — **4/5**

A Seção 6.1 é um dos pontos mais fortes do paper. Os autores enumeram explicitamente: escopo restrito, critério de convergência heurístico, ambiente sem tráfego de fundo, dependência de modelo único, validade interna comprometida pelo Entity Flood, e validade externa limitada pela natureza LLM-gerada das variantes. Esta honestidade epistêmica é bem-vinda e rara.

Ponto omitido: não é discutido o risco de que as técnicas de evasão no catálogo do Agente de Ataque tenham sido derivadas de corpus de treinamento do próprio DeepSeek V4 Pro, criando um potencial viés de circularidade (o mesmo modelo defende e ataca).

**Nota Consolidada Critério 5: 3/5**

---

## CRITÉRIO 6 — FIGURAS, GRÁFICOS E TABELAS

### Figura 1 — Diagrama de arquitetura

**Valor:** Adequado — comunica o fluxo principal do ciclo. **Qualidade técnica:** Os rótulos dos componentes internos são identificáveis. Contudo, a figura é um "boxes and arrows" de alto nível; não especifica fluxos de dados entre componentes (e.g., o que exatamente o Orquestrador envia ao Agente de Defesa no "histórico acumulado de falhas"?). **Nota: 3/5**

### Figura 2 — Evolução da competição adversarial (7 painéis)

**Valor:** Alta — esta é a visualização central do paper. Os dois eixos (execução adversarial × taxa acumulada) com duas curvas (detecção em verde, evasão em vermelho) e região sombreada para fase base comunicam claramente a dinâmica do ciclo adversarial. **Qualidade técnica:** Eixos rotulados adequadamente. A escala do eixo X varia entre painéis (o Entity Flood chega a 72 execuções vs 27 do MQTT QoS), o que é correto mas poderia ser explicitado na caption. O tamanho reduzido dos painéis em layout 2×3+1 prejudica a legibilidade do eixo X quando impresso em coluna dupla. **Integridade:** Sem cherry-picking aparente — o Entity Flood (pior caso) está incluído. **Nota: 4/5**

### Figura 3 — Matrizes de cobertura regras × variantes (7 painéis)

**Valor:** Alto para análise temporal do ciclo adversarial. **Qualidade técnica:** Criticamente, os rótulos dos eixos (número de regras, número de variantes) são ilegíveis no tamanho de impressão. O título de cada painel está visível mas os eixos não têm unidades ou escala explícita. A legenda (h) é clara, mas a escala das matrizes varia muito entre painéis sem nota explicativa. **Nota: 2/5**

### Tabela 1 — Comparativo de trabalhos relacionados

Avaliada no Critério 3. **Nota: 2/5**

### Tabela 2 — Cenários de ataque

Clara e adequada. **Nota: 4/5**

### Tabela 3 — Métricas da competição adversarial

Apresentação clara com métricas IC, Variantes, TDV%, TE% e Regras. A nota de rodapé sobre o Entity Flood é essencial e bem posicionada. A ausência de intervalos de confiança é a principal fragilidade (coberta no Critério 5). **Nota: 3/5**

**Nota Consolidada Critério 6: 3/5**

---

## CRITÉRIO 7 — QUALIDADE DA ESCRITA E ORGANIZAÇÃO

- **Estrutura lógica:** O paper segue a progressão clássica Intro → Background → Trabalhos Relacionados → Metodologia → Resultados → Conclusão de forma coerente. A Seção 2 (Fundamentação Teórica) é funcional mas poderia ser integrada ao contexto sem seção separada, dado o espaço limitado.
- **Precisão técnica:** A terminologia é usada de forma consistente ao longo do texto (Agente de Defesa, Agente de Ataque, IC, TDV, TE). Não foram identificados usos inconsistentes ou incorretos de termos técnicos.
- **Clareza:** O paper é bem escrito em português técnico. A Seção 5.2 é densa em análise, mas a segmentação em subseções (5.2.1–5.2.5) torna a leitura gerenciável.
- **Autocontenção da prova de conceito:** Os autores são disciplinados em sempre qualificar os resultados como "prova de conceito" e "caráter exploratório" — isso é epistemicamente correto e honesto.
- **Formatação:** Aparentemente dentro das diretrizes SBSeg (2 colunas, referências no formato da conferência).

**Nota Consolidada Critério 7: 4/5**

---

## SUMÁRIO DA REVISÃO

| Critério                        | Nota (1–5) | Síntese                                                                 |
|--------------------------------|------------|-------------------------------------------------------------------------|
| 1. Anonimidade                 | 1 — FALHA  | URL GitHub com username identificável (cwrricio) na nota de rodapé 2    |
| 2. Introdução                  | 3          | Motivação presente mas sem métricas externas; contribuições sem quantificação |
| 3. Trabalhos Relacionados      | 2          | Tabela com colunas triviais; discussão rasa; dimensões técnicas ausentes |
| 4. Metodologia / Design        | 3          | Design claro mas sem threat model formal e sem prompts divulgados        |
| 5. Avaliação / Resultados      | 3          | Sem IC/erro padrão; sem FP; modelo único; sem baseline competidor justo  |
| 6. Figuras, Gráficos, Tabelas  | 3          | Figura 2 informativa; Figura 3 com legibilidade crítica; Tabela 1 fraca |
| 7. Qualidade da Escrita        | 4          | Bem estruturado, terminologia consistente, honestidade epistêmica        |

**NOTA GERAL** (média ponderada, critério 3 com peso 2x):

```
Numerador  = 1 + 3 + (2×2) + 3 + 3 + 3 + 4 = 21
Denominador = 1 + 1 + 2 + 1 + 1 + 1 + 1 = 8
NOTA GERAL = 21 / 8 = 2,63 / 5
```

---

## PONTOS FORTES

1. **Inovação na modalidade de validação:** A abordagem de validação dinâmica adversarial em tempo real — com implantação em instância Snort real e execução de ataques via Docker — é tecnicamente diferenciada em relação ao estado da arte. Nenhum dos trabalhos comparados opera sob este paradigma.

2. **Honestidade epistêmica e rigor nas limitações:** A Seção 6.1 é exemplar: os autores enumeram proativamente seis classes de ameaças à validade (escopo, critério heurístico, ambiente controlado, dependência de modelo, validade interna, validade externa), incluindo o caso de não-convergência do Entity Flood. Esta transparência é rara e valiosa.

3. **Confirmação experimental da lacuna de cobertura IoT:** O resultado "zero alertas das regras comunitárias Snort para todos os sete cenários IoT testados" é simples, direto e empiricamente impactante — constitui o argumento mais forte do paper para motivar a linha de pesquisa.

4. **Métricas complementares bem projetadas:** A combinação IC + TDV + TE permite análise multidimensional da dinâmica adversarial (custo de síntese × generalização × vulnerabilidade), e as matrizes de cobertura da Figura 3 fornecem visão granular do ciclo temporal.

---

## PONTOS FRACOS / QUESTÕES OBRIGATÓRIAS PARA OS AUTORES

1. **[crítico] Violação de anonimidade** — O URL `https://github.com/cwrricio/ataques-sbseg26` na nota de rodapé 2 expõe um username GitHub (cwrricio) potencialmente rastreável à identidade dos autores, e o nome do repositório menciona explicitamente a venue (sbseg26). Para resubmissão, o link deve ser substituído por uma URL anonimizada (e.g., repositório criado em conta dedicada sem histórico identificador) ou removido com referência genérica ao material suplementar.

2. **[crítico] Ausência de avaliação de falsos positivos** — Nenhuma métrica de FP é reportada. O paper cita "tráfego benigno para evitar FPs" mas não quantifica a taxa de FP das regras geradas sob tráfego legítimo. Uma regra Snort que detecta 90% dos ataques mas dispara em 40% do tráfego legítimo é inoperacional em produção. É necessário medir e reportar a taxa de falso positivo de cada regra gerada, ao menos em um subconjunto representativo.

3. **[crítico] Ausência de threat model formal** — O paper carece de uma seção de modelo de ameaça explícita que defina: (a) o que o adversário conhece sobre o IDS (black/grey/white-box); (b) as capacidades de rede do adversário; (c) o objetivo formal do adversário (evadir detecção? comprometer disponibilidade do IDS?). Esta definição é pré-requisito para avaliar se o Agente de Ataque operacionaliza de forma fiel o adversário declarado.

4. **[crítico] Tabela comparativa (Critério 3) insuficiente** — A coluna "Usa LLMs" deve ser removida por ser trivialmente não-discriminativa no contexto 2025–2026. Novas colunas essenciais: protocolo/domínio alvo; avaliação de FP (sim/não/não relatado); modelo de ameaça (passivo/ativo); e número de cenários avaliados. A tabela atual não permite ao leitor entender o posicionamento da proposta de forma estruturada.

5. **[crítico] Ausência de intervalos de confiança e análise de significância** — Com LLMs envolvidos (mesmo a temperatura 0), os resultados de IC, TDV e TE devem ser reportados com variância de pelo menos 3 execuções independentes por cenário. Resultados pontuais de uma única execução não permitem distinguir comportamento sistemático de artefato de execução.

6. **[sugerido] Avaliação com múltiplos modelos LLM** — O paper usa exclusivamente DeepSeek V4 Pro. Um ablation com ao menos um modelo adicional (e.g., GPT-4o ou Claude Sonnet) permitiria avaliar se os resultados são específicos ao modelo ou generalizáveis à abordagem arquitetural. Sem isso, os resultados são condicionados a uma única escolha de modelo.

7. **[sugerido] Legibilidade das matrizes de cobertura (Figura 3)** — Os eixos das matrizes são ilegíveis no tamanho de coluna dupla. Considerar aumentar os painéis, reduzir o número de painéis por figura ou publicar em formato suplementar com escala adequada.

8. **[sugerido] Divulgação dos templates de prompt** — Os system prompts dos agentes (Defesa e Ataque) têm impacto direto nos resultados e constituem o "código-fonte" do sistema. Sem divulgação, a reprodutibilidade é comprometida. Incluir no apêndice ou repositório.

---

## RECOMENDAÇÃO

**[ Reject ]**

**Justificativa:** A violação de anonimidade na nota de rodapé 2 (URL GitHub com username `cwrricio`) constitui falha de pré-condição que, per os critérios desta revisão no padrão USENIX Security/NDSS, implica rejeição direta desta submissão. Adicionalmente, mesmo sanada a questão de anonimidade, o paper apresenta lacunas técnicas substantivas que demandam revisão maior antes de aceitação: (1) ausência completa de avaliação de falsos positivos para um sistema de IDS — métrica central de qualidade operacional; (2) ausência de threat model formal, pré-requisito para papers de segurança em tier-1; (3) tabela comparativa com colunas trivialmente não-discriminativas que não sustenta o posicionamento da contribuição; (4) resultados sem intervalos de confiança provenientes de execução única com modelo único. O trabalho possui mérito técnico genuíno — a arquitetura adversarial para validação dinâmica de regras Snort em IoT é uma contribuição diferenciada — e é encorajada a resubmissão após correção das questões críticas enumeradas, com ênfase na adição de avaliação de FP, threat model e rigor estatístico.

---

*Revisão gerada em conformidade com o prompt revisor_v1.md. Nível de rigor: USENIX Security / NDSS / SIGCOMM.*
