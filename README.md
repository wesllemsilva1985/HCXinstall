<h2>Script de Instalação Automática para HCXdumpTool/HCXtool</h2>

<!-- wp:tadv/classic-paragraph -->
<p>O HCXinstall é um script desenvolvido em Python para facilitar a instalação dos pacotes hcxdumptool e hcxtool no Kali Linux, necessários para captura do PMKID.</p>
<!-- /wp:tadv/classic-paragraph -->

<!-- wp:tadv/classic-paragraph -->
<h3>PMKID</h3>
<p>Jens “Atom” Steube, responsável pelo desenvolvimento da ferramenta Hashcat, descobriu uma nova técnica que pode ser usada para quebrar facilmente as senhas WiFi da maioria dos routers modernos.</p>
<p>A nova técnica permite quebrar os protocolos de rede sem fio WPA / WPA2 com os recursos de roaming Pairwise Master Key Identifier (PMKID) ativos.</p>
<p>O especialista analisava o padrão de segurança WPA3 quando acidentalmente “identificou e desenvolveu uma nova técnica”.</p>
<p>Antes as técnicas de ataque exigiam a captura de um handshake(aperto de mão) completo de 4 vias do Protocolo de Autenticação Extensível via LAN (EAPOL), que é um protocolo de autenticação de porta de rede. A nova técnica de ataque, diferente das anteriores, tem como alvo o Elemento de Informação de Rede Robust Secure (RSN IE).</p>
<p>O protocolo RSN foi projetado para estabelecer comunicações seguras numa rede sem fios 802.11 e faz parte do padrão 802.11i (WPA). Então sempre que tenta estabelecer um canal de comunicação seguro, o RSN transmite uma mensagem do RSN IE dentro da rede.</p>
<figure class="wp-block-image"><img src="https://i0.wp.com/seguranca-informatica.pt/wp-content/uploads/2018/08/wifi-hacking.png?zoom=1.100000023841858&amp;w=750&amp;ssl=1" alt="wifi-hacking" width="630" height="468" src-orig="https://i0.wp.com/seguranca-informatica.pt/wp-content/uploads/2018/08/wifi-hacking.png?w=750&amp;ssl=1" scale="1.100000023841858" />
<figcaption></figcaption>
</figure>
<p>O protocolo Robust Security Network possui o PMKID (Pairwise Master Key Identifier), que é a chave necessária para estabelecer uma conexão entre um cliente e um ponto de acesso.</p>
<!-- /wp:tadv/classic-paragraph -->

<!-- wp:tadv/classic-paragraph -->
<h3>Clonar HCXinstall</h3>
<p>Download no <a href="https://github.com/igorMatsunaga/HCXinstall">github</a> ou diretamente pelo terminal utilizando o comando:</p>
<!-- /wp:tadv/classic-paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>git clone https://github.com/igorMatsunaga/HcXinstall</code></pre>
<!-- /wp:code -->

<!-- wp:tadv/classic-paragraph -->
<h3>Utilizar</h3>
<p>Navegue até o  local onde foi realizado o download do hcxinstall e execute o comando:</p>
<!-- /wp:tadv/classic-paragraph -->

<!-- wp:code -->
<pre class="wp-block-code"><code>python hcxInstall.py</code></pre>
<!-- /wp:code -->

<!-- wp:tadv/classic-paragraph -->
<p>Escolha o número da opção que deseja utilizar e o script se encarregará do resto para você:</p>
<p>(1) Instalar Hcxdumptool<br />(2) Instalar hxctools<br />(3) Instalar Hcxdumptool e hxctools</p>
<!-- /wp:tadv/classic-paragraph -->

<!-- wp:image {"id":3033} -->
<figure class="wp-block-image"><img src="https://nsworld.com.br/wp-content/uploads/2019/06/hcxinstall.png" alt="" class="wp-image-3033"/></figure>
<!-- /wp:image -->

<!-- wp:paragraph -->
<p></p>
<!-- /wp:paragraph -->
