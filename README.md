<h1>Desafio 8 - Acessando e modificando a lista</h1>
<p>
  
  O código inicia com uma lista de frutas e, em seguida, realiza duas modificações importantes:

<li>O índice da palavra "banana" é encontrado utilizando index() e é então substituído por "morango".</li>

<li>
    A palavra "abacaxi" é adicionada ao final da lista usando append().
  Essas modificações são seguidas pela impressão da lista de frutas atualizada, proporcionando uma visão completa das alterações efetuadas.
</li>
  
</p>

<ol>
  
  <h2><li>Criação da Lista de Frutas:</li></h2>
  <ul>
    <li>frutas = ['maça', 'banana', 'manga', 'uva', 'abacaxi']: Uma lista inicial de frutas é criada.</li>
  </ul>

  <h2><li>Modificação da Lista:</li></h2>
  <ul>
    <li>posicao = frutas.index('banana'): A função index() é utilizada para encontrar o índice da palavra "banana" na lista e armazenar esse valor em posicao.</li>
    <li>
      frutas[posicao] = 'morango': O elemento na posição encontrada é substituído por "morango".
    </li>
    <li>
      frutas.append('abacaxi'): A palavra "abacaxi" é adicionada ao final da lista usando o método append().
    </li>
  </ul>

  <h2><li>Saída de Dados:</li></h2>
  <ul>
    <li>print(frutas): A lista modificada é exibida na saída padrão, mostrando as alterações realizadas.</li>
  </ul>
</ol>