# Técnica de Ingeniería de Prompt: CETO

La técnica CETO es un enfoque estructurado para diseñar prompts eficaces en sistemas de inteligencia artificial, especialmente en modelos de lenguaje. CETO es un acrónimo que representa cuatro componentes clave: **Contexto**, **Ejemplo**, **Tarea** y **Objetivo**. Cada uno cumple una función específica para guiar al modelo hacia respuestas más precisas, útiles y alineadas con la intención del usuario.

## Componentes de CETO

### 1. Contexto
El **Contexto** proporciona al modelo la información de fondo necesaria para interpretar adecuadamente la solicitud. Incluye detalles relevantes, antecedentes del tema, restricciones del dominio o cualquier otra información que permita situar la conversación en el entorno adecuado.

- Establece las bases temáticas o situacionales.
- Ayuda al modelo a desambiguar términos o instrucciones.

### 2. Ejemplo
La sección de **Ejemplo** muestra al modelo un patrón de respuesta esperado o una demostración representativa de cómo debe realizar la tarea.

- Refuerza el comportamiento deseado.
- Aumenta la precisión en tareas repetitivas o estilísticas.
- Puede incluir entradas y salidas simuladas si es necesario.

### 3. Tarea
La **Tarea** define con claridad qué debe hacer el modelo. Debe redactarse de manera directa y específica, evitando ambigüedades.

- Describe la acción solicitada (resumir, traducir, analizar, clasificar, etc.).
- Incluye verbos operativos claros y delimitaciones si las hay.

### 4. Objetivo
El **Objetivo** establece la finalidad o meta última de la tarea. Este componente permite que el modelo alinee su comportamiento con el propósito final.

- Clarifica el por qué detrás de la tarea.
- Aumenta la relevancia de la respuesta en función del uso esperado.

## Funcionamiento de CETO

El proceso de construcción de prompts usando CETO consiste en ensamblar los cuatro elementos en un orden lógico y cohesivo. Aunque el orden puede variar según el caso de uso, una secuencia típica podría ser: **Contexto → Ejemplo → Tarea → Objetivo**.

El diseño cuidadoso de cada componente ayuda al modelo a:

- Comprender mejor las expectativas del usuario.
- Minimizar errores de interpretación.
- Producir resultados más consistentes y adecuados.

CETO es especialmente útil en entornos donde se requiere precisión, control y trazabilidad del comportamiento de un modelo de lenguaje. Esta técnica facilita la sistematización del diseño de prompts y mejora la reproducibilidad de resultados en entornos profesionales o de investigación.
---


# Técnica de Ingeniería de Prompt: ASPECCT

La técnica **ASPECCT** es un modelo estructurado para diseñar prompts claros y eficaces, orientado a profesionales que requieren transformar información extensa o dispersa en textos sintéticos y bien organizados. ASPECCT se compone de siete elementos fundamentales: **Action**, **Step**, **Person**, **Example**, **Context**, **Constrains** y **Template**.

## Componentes de ASPECCT

### 1. Action (Acción)
Define el tipo de tarea que el modelo debe realizar. En este caso, las acciones clave son redactar y sintetizar. Esto implica transformar insumos informativos en textos claros, precisos y bien estructurados.

### 2. Step (Pasos)
Detalla el procedimiento que debe seguir el modelo para cumplir la acción de forma efectiva:

- Analizar la información proporcionada.
- Identificar los puntos clave del contenido.
- Redactar un texto coherente y claro que resuma la información.
- Usar un tono formal y objetivo.

Estos pasos aseguran una metodología consistente y orientada a la claridad comunicativa.

### 3. Person (Perfil del redactor)
Especifica el perfil que el modelo debe emular. En ASPECCT, se asume el rol de un redactor profesional especializado en comunicación empresarial, capaz de adaptar su lenguaje a distintos públicos sin perder precisión ni formalidad.

### 4. Example (Ejemplo de aplicación)
Refiere a los tipos de textos que sirven como referencia para el estilo y la estructura de salida esperada:

- Resumen ejecutivo de un informe de sostenibilidad.
- Síntesis de una reunión de trabajo.
- Boletín interno dirigido a empleados.

Esto define un marco práctico de generación textual profesional.

### 5. Context (Contexto)
Describe la situación de uso: el usuario entrega insumos como notas de reunión, informes u otros documentos extensos, y necesita comunicar los puntos más relevantes de manera clara y concisa a una audiencia específica como directivos, empleados o clientes.

### 6. Constrains (Restricciones)
Establece los límites que debe respetar la generación textual:

- Máximo 300 palabras.
- Lenguaje claro, sin tecnicismos.
- Estructura lógica (introducción, desarrollo, cierre).
- Evitar juicios personales u opiniones.

Estas restricciones garantizan la efectividad comunicativa del resultado.

### 7. Template (Plantilla)
Proporciona un formato predefinido para estructurar el texto de salida. El modelo debe seguir esta estructura:

'scss  
[Título del texto]

[Introducción breve: 2-3 oraciones para contextualizar el tema]

[Desarrollo: Enumerar o explicar los puntos clave de manera clara y ordenada]

[Conclusión: cierre con mensaje final, llamado a la acción o resumen breve]

(Fecha - Autor o entidad, si se requiere)  
'

## Funcionamiento de ASPECCT

ASPECCT opera como una guía detallada para construir prompts efectivos centrados en tareas de redacción ejecutiva. Al definir con precisión el tipo de acción, los pasos a seguir, el perfil del redactor, los ejemplos de referencia, el contexto de uso, las restricciones y la plantilla estructural, se logra un alto grado de control sobre el estilo, contenido y forma de las respuestas generadas. Esta técnica es especialmente útil en entornos empresariales donde la claridad, la brevedad y la precisión son fundamentales.


