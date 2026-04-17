<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
    <title>VetDosis - Calculadora de medicamentos para perros y gatos</title>
    <style>
        * {
            box-sizing: border-box;
            font-family: system-ui, 'Segoe UI', 'Roboto', 'Helvetica Neue', sans-serif;
        }
        body {
            background: #e9f0f5;
            margin: 0;
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        .app-card {
            background: white;
            border-radius: 32px;
            box-shadow: 0 12px 30px rgba(0,0,0,0.1);
            overflow: hidden;
            margin-bottom: 30px;
        }
        .header {
            background: #2c5f2d;
            color: white;
            padding: 20px 28px;
        }
        .header h1 {
            margin: 0;
            font-size: 1.8rem;
        }
        .header p {
            margin: 8px 0 0;
            opacity: 0.85;
            font-size: 0.95rem;
        }
        .disclaimer {
            background: #fff3cd;
            border-left: 6px solid #f0ad4e;
            padding: 12px 20px;
            margin: 20px 28px;
            border-radius: 20px;
            color: #856404;
            font-size: 0.85rem;
            font-weight: 500;
        }
        .form-section {
            padding: 20px 28px;
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap: 24px;
            border-bottom: 1px solid #dee2e6;
        }
        .input-group {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }
        .input-group label {
            font-weight: 700;
            color: #1e3c2c;
            display: flex;
            align-items: center;
            gap: 6px;
        }
        .input-group label i {
            font-style: normal;
            font-weight: normal;
        }
        select, input {
            padding: 12px 14px;
            border: 1.5px solid #ced4da;
            border-radius: 24px;
            font-size: 1rem;
            background: #fff;
            transition: 0.2s;
        }
        select:focus, input:focus {
            border-color: #2c5f2d;
            outline: none;
            box-shadow: 0 0 0 3px rgba(44,95,45,0.2);
        }
        .warning-badge {
            background: #f8d7da;
            color: #721c24;
            border-radius: 40px;
            padding: 4px 12px;
            font-size: 0.75rem;
            font-weight: bold;
            display: inline-block;
            margin-top: 6px;
        }
        .btn-calcular {
            background: #2c5f2d;
            color: white;
            border: none;
            padding: 14px 28px;
            border-radius: 40px;
            font-weight: bold;
            font-size: 1.1rem;
            cursor: pointer;
            transition: 0.2s;
            margin: 20px 28px;
            width: calc(100% - 56px);
            box-shadow: 0 2px 6px rgba(0,0,0,0.1);
        }
        .btn-calcular:hover {
            background: #1f4520;
            transform: scale(1.01);
        }
        .results-section {
            padding: 10px 28px 30px;
        }
        .med-list {
            display: flex;
            flex-direction: column;
            gap: 20px;
        }
        .med-card {
            background: #fef9e8;
            border-radius: 28px;
            padding: 18px 22px;
            border-left: 8px solid #97bc62;
            box-shadow: 0 4px 8px rgba(0,0,0,0.03);
        }
        .med-name {
            font-size: 1.4rem;
            font-weight: 800;
            color: #1f3b2c;
            margin-bottom: 6px;
        }
        .med-dose {
            font-size: 1.1rem;
            font-weight: 600;
            background: #eef2e6;
            display: inline-block;
            padding: 6px 16px;
            border-radius: 50px;
            margin: 10px 0 8px;
        }
        .med-warning {
            background: #fff0f0;
            border-radius: 20px;
            padding: 12px 16px;
            margin-top: 12px;
            color: #b33;
            font-size: 0.85rem;
            font-weight: 500;
        }
        .med-safe {
            color: #2c5f2d;
            background: #e1f3e1;
        }
        hr {
            margin: 20px 0;
        }
        .footer-note {
            font-size: 0.7rem;
            text-align: center;
            padding: 15px;
            color: #6c757d;
        }
        @media (max-width: 700px) {
            .form-section { padding: 20px; }
            .med-name { font-size: 1.2rem; }
        }
    </style>
</head>
<body>
<div class="container">
    <div class="app-card">
        <div class="header">
            <h1>🐾 VetDosis • Farmacología veterinaria</h1>
            <p>Dosis personalizadas según especie, peso, edad, raza y estado reproductivo</p>
        </div>
        <div class="disclaimer">
            ⚠️ ADVERTENCIA: Esta herramienta es solo de referencia educativa. Las dosis deben ser ajustadas y autorizadas por un veterinario. No reemplaza el criterio clínico. Los errores de dosificación pueden ser fatales.
        </div>
        <div class="form-section">
            <div class="input-group">
                <label>🐕 Especie</label>
                <select id="especie">
                    <option value="perro">Perro</option>
                    <option value="gato">Gato</option>
                </select>
            </div>
            <div class="input-group">
                <label>⚖️ Peso (kg)</label>
                <input type="number" id="peso" step="0.1" value="10" min="0.5">
            </div>
            <div class="input-group">
                <label>📅 Edad</label>
                <select id="edad">
                    <option value="cachorro">Cachorro (&lt;6 meses)</option>
                    <option value="adulto" selected>Adulto (6 meses - 8 años)</option>
                    <option value="geriátrico">Geriatrico (&gt;8 años)</option>
                </select>
            </div>
            <div class="input-group">
                <label>🧬 Raza (perros)</label>
                <input type="text" id="raza" placeholder="Ej: Border Collie, Pastor Australiano, Lab..." value="Border Collie">
                <span class="warning-badge" id="razaWarning" style="display:none;">⚠️ Posible portador MDR1</span>
            </div>
            <div class="input-group">
                <label>🤰 Estado reproductivo</label>
                <select id="estadoRepro">
                    <option value="neutro">Castrado/esterilizado</option>
                    <option value="entero">Entero (sin castrar)</option>
                    <option value="gestante">Gestante (preñada)</option>
                    <option value="lactante">Lactante</option>
                </select>
            </div>
        </div>
        <button class="btn-calcular" id="calcularBtn">💊 Calcular dosis seguras</button>
        <div class="results-section" id="results">
            <div style="text-align: center; color: #5f6c5b; padding: 20px;">Completa los datos y presiona calcular</div>
        </div>
        <div class="footer-note">
            * Información basada en referencias veterinarias. Las dosis se expresan como rango terapéutico (mg/kg).<br>
            Razas MDR1: Collie, Pastor Australiano, Shetland, Pastor Inglés, Border Collie, entre otras → riesgo con ivermectina, loperamida.
        </div>
    </div>
</div>

<script>
    // --------------------------------------------------------------
    // BASE DE DATOS DE MEDICAMENTOS (simula extracción desde web/API)
    // --------------------------------------------------------------
    const medicamentosDB = [
        {
            nombre: "💊 Amoxicilina + Ác. Clavulánico",
            principio: "amoxicilina",
            dosisRango: { min: 10, max: 20 },  // mg/kg
            unidad: "mg/kg c/12h",
            especies: ["perro", "gato"],
            contraindicaciones: {
                gestante: false,   // false = no contraindicado absoluto, pero precaución; usaremos advertencia
                lactante: false,
                cachorro: false,
                razaMDR1: false,
                geriatrico: false,
                requiereAjusteRenal: true
            },
            nota: "Usar con precaución en animales con insuficiencia renal. No es ototóxico."
        },
        {
            nombre: "💧 Meloxicam (AINE)",
            principio: "meloxicam",
            dosisRango: { min: 0.05, max: 0.1 },  // dosis inicial 0.1 mantenimiento 0.05
            unidad: "mg/kg (cada 24h, máximo 3-5 días)",
            especies: ["perro", "gato"],
            contraindicaciones: {
                gestante: true,
                lactante: true,
                cachorro: true,
                razaMDR1: false,
                geriatrico: true   // ajustar dosis, riesgo incrementado
            },
            nota: "Contraindicado en gatos deshidratados o con enfermedad renal. En gatos usar una sola dosis. No en cachorros <6 semanas."
        },
        {
            nombre: "🪱 Ivermectina (antiparasitario)",
            principio: "ivermectina",
            dosisRango: { min: 0.2, max: 0.4 },
            unidad: "mg/kg (vía subcutánea u oral)",
            especies: ["perro", "gato"],
            contraindicaciones: {
                gestante: true,
                lactante: true,
                cachorro: false,
                razaMDR1: true,
                geriatrico: false
            },
            nota: "⚠️ TOXICIDAD SEVERA en razas con mutación MDR1. Nunca usar en Collie, Pastor Australiano, etc. sin prueba genética."
        },
        {
            nombre: "🤢 Maropitant (antiemético)",
            principio: "maropitant",
            dosisRango: { min: 1, max: 1 },
            unidad: "mg/kg c/24h",
            especies: ["perro", "gato"],
            contraindicaciones: {
                gestante: false,
                lactante: false,
                cachorro: false,
                razaMDR1: false,
                geriatrico: false
            },
            nota: "Seguro en cachorros desde 8 semanas. Usar con precaución en hepatopatías."
        },
        {
            nombre: "🧫 Metronidazol",
            principio: "metronidazol",
            dosisRango: { min: 10, max: 15 },
            unidad: "mg/kg c/12h",
            especies: ["perro", "gato"],
            contraindicaciones: {
                gestante: false,
                lactante: true,  // evitar en lactancia si es posible
                cachorro: false,
                razaMDR1: false,
                geriatrico: false
            },
            nota: "Puede causar neurotoxicidad a dosis altas. Evitar en gestantes tempranas."
        }
    ];

    // Lista de palabras clave para razas MDR1 (sensibilidad a ivermectina y otros)
    const razasMDR1 = [
        "border collie", "collie", "pastor australiano", "australian shepherd", "shetland sheepdog",
        "old english sheepdog", "pastor inglés", "rough collie", "smooth collie", "longhaired whippet",
        "german shepherd" // con menor frecuencia pero algunos estudios
    ];

    // Función para verificar si una raza ingresada tiene riesgo MDR1
    function checkMDR1(razaInput) {
        if (!razaInput) return false;
        const razaLower = razaInput.toLowerCase().trim();
        return razasMDR1.some(r => razaLower.includes(r));
    }

    // Determina si el medicamento tiene contraindicación según perfil del paciente
    function getMedicamentoStatus(med, especie, edad, estadoRepro, esRazaMDR1, pesoKg) {
        let warnings = [];
        let contraindicated = false;
        let doseAdjustMsg = "";

        // 1. Restricción por especie (ya filtramos en la lista)
        if (!med.especies.includes(especie)) {
            return { disponible: false, motivo: "No indicado para esta especie" };
        }

        // 2. Edad cachorro y AINEs / otros
        if (edad === "cachorro" && med.contraindicaciones.cachorro) {
            warnings.push("❌ Contraindicado en cachorros (riesgo de úlceras/daño renal).");
            contraindicated = true;
        }
        // 3. Estado reproductivo
        if (estadoRepro === "gestante" && med.contraindicaciones.gestante) {
            warnings.push("🚫 Contraindicado durante la gestación (riesgo fetal).");
            contraindicated = true;
        }
        if (estadoRepro === "lactante" && med.contraindicaciones.lactante) {
            warnings.push("⚠️ Evitar durante la lactancia (excreción en leche).");
            contraindicated = true;
        }
        // 4. Raza MDR1 + Ivermectina o cualquier medicamento con flag
        if (esRazaMDR1 && med.contraindicaciones.razaMDR1) {
            warnings.push("🧬 ALERTA: Raza con predisposición MDR1. Altísimo riesgo de neurotoxicidad. NO administrar ivermectina.");
            contraindicated = true;
        }
        // 5. Geriátrico y AINEs (meloxicam)
        if (edad === "geriátrico" && med.contraindicaciones.geriátrico && med.principio === "meloxicam") {
            warnings.push("👴 Paciente geriátrico: usar dosis mínima, monitorizar función renal.");
            doseAdjustMsg = "Dosis sugerida: 0.05 mg/kg cada 48h bajo supervisión.";
        }
        // Advertencia adicional para gatos con meloxicam
        if (especie === "gato" && med.principio === "meloxicam") {
            warnings.push("🐱 En gatos, meloxicam es de uso único (dosis única) o extrema precaución. Evitar tratamientos prolongados.");
        }
        // Ajuste por peso extremo
        if (pesoKg < 2 && med.principio !== "maropitant") {
            warnings.push("⚡ Peso muy bajo: verificar dilución y jeringa de insulina. Riesgo de sobredosis.");
        }

        // Cálculo de dosis sugerida en mg total y presentación práctica
        let dosisMinMg = med.dosisRango.min * pesoKg;
        let dosisMaxMg = med.dosisRango.max * pesoKg;
        let dosisMediaMg = (dosisMinMg + dosisMaxMg) / 2;
        
        // Texto de dosis orientativa
        let dosisTexto = `${dosisMinMg.toFixed(1)} - ${dosisMaxMg.toFixed(1)} mg total (${med.dosisRango.min}-${med.dosisRango.max} mg/kg) cada dosis. ${med.unidad}`;
        if (doseAdjustMsg) dosisTexto += ` | ${doseAdjustMsg}`;
        
        return {
            disponible: true,
            contraindicated: contraindicated,
            warnings: warnings,
            dosisTexto: dosisTexto,
            dosisMedia: dosisMediaMg.toFixed(1),
            nombre: med.nombre
        };
    }

    // Mostrar resultados en el DOM
    function renderResults(especie, peso, edad, estadoRepro, raza, esRazaMDR1) {
        const resultsDiv = document.getElementById("results");
        if (!peso || peso <= 0) {
            resultsDiv.innerHTML = `<div class="med-card" style="background:#ffe6e6;"><div class="med-name">⚠️ Error</div>Ingresa un peso válido mayor a 0 kg.</div>`;
            return;
        }

        // Filtrar medicamentos por especie y generar tarjetas
        let medicamentosFiltrados = medicamentosDB.filter(med => med.especies.includes(especie));
        
        if (medicamentosFiltrados.length === 0) {
            resultsDiv.innerHTML = `<div class="med-card">No hay medicamentos disponibles para esta especie en la demo.</div>`;
            return;
        }

        let html = `<div class="med-list">`;
        for (let med of medicamentosFiltrados) {
            const status = getMedicamentoStatus(med, especie, edad, estadoRepro, esRazaMDR1, peso);
            if (!status.disponible) {
                html += `
                    <div class="med-card" style="border-left-color: #aaa; background:#f2f2f2;">
                        <div class="med-name">${med.nombre}</div>
                        <div class="med-warning">🚫 ${status.motivo}</div>
                    </div>`;
                continue;
            }
            let warningHtml = "";
            if (status.warnings.length > 0) {
                warningHtml = `<div class="med-warning">${status.warnings.join("<br>")}</div>`;
            }
            let extraClass = status.contraindicated ? "med-warning" : "";
            let borderColor = status.contraindicated ? "#dc3545" : "#97bc62";
            html += `
                <div class="med-card" style="border-left-color: ${borderColor};">
                    <div class="med-name">${med.nombre}</div>
                    <div class="med-dose">💉 Dosis orientativa: ${status.dosisTexto}</div>
                    ${status.contraindicated ? `<div class="med-warning" style="background:#f5c6cb; color:#721c24;">⛔ CONTRAINDICADO: No administrar según perfil del paciente.</div>` : ""}
                    ${warningHtml}
                    <div style="font-size:0.75rem; margin-top:8px; color:#6c5b3a;">📌 ${med.nota}</div>
                </div>
            `;
        }
        html += `</div><hr><div style="font-size:0.8rem; background:#eef; padding:12px; border-radius:20px;">🔍 <strong>Resumen restricciones</strong><br>
                - Edad: ${edad === "cachorro" ? "Evitar AINEs y ciertos fármacos." : edad === "geriátrico" ? "Ajustar dosis de AINEs." : "Sin restricción etaria especial."}<br>
                - Estado reproductivo: ${estadoRepro === "gestante" ? "Evitar ivermectina, meloxicam y metronidazol (valorar riesgo)." : estadoRepro === "lactante" ? "Precaución con metronidazol y meloxicam." : "Sin restricción principal."}<br>
                - Raza MDR1: ${esRazaMDR1 ? "⚠️ ALTA SENSIBILIDAD - Ivermectina y otros fármacos contraindicados." : "No se detectó raza de riesgo MDR1 (si es mestizo, considerar test genético)."}<br>
                - Peso: ${peso} kg → dosis calculadas en rango seguro.
                </div>`;
        resultsDiv.innerHTML = html;
    }

    // Evento principal
    document.getElementById("calcularBtn").addEventListener("click", function() {
        const especie = document.getElementById("especie").value;
        let peso = parseFloat(document.getElementById("peso").value);
        if (isNaN(peso) || peso <= 0) peso = 1;
        const edad = document.getElementById("edad").value;
        const estadoRepro = document.getElementById("estadoRepro").value;
        let razaInput = document.getElementById("raza").value;
        const esRazaMDR1 = checkMDR1(razaInput);
        
        // Mostrar warning visual en tiempo real (actualizar badge)
        const badge = document.getElementById("razaWarning");
        if (esRazaMDR1 && especie === "perro") {
            badge.style.display = "inline-block";
            badge.innerText = "⚠️ Posible portador MDR1 (riesgo con ivermectina)";
        } else {
            badge.style.display = "none";
        }
        
        // Extra validación gatos: raza no aplica para MDR1 pero igual se muestra
        if (especie === "gato") {
            badge.style.display = "none";
        }
        
        renderResults(especie, peso, edad, estadoRepro, razaInput, esRazaMDR1 && especie === "perro");
    });

    // Actualización visual al cambiar especie (reset de mensaje MDR1)
    document.getElementById("especie").addEventListener("change", function(e) {
        const especie = e.target.value;
        const badge = document.getElementById("razaWarning");
        if (especie === "gato") {
            badge.style.display = "none";
            document.getElementById("raza").placeholder = "Solo relevante en perros";
        } else {
            document.getElementById("raza").placeholder = "Ej: Border Collie, Pastor Australiano...";
            const razaActual = document.getElementById("raza").value;
            if (checkMDR1(razaActual)) badge.style.display = "inline-block";
            else badge.style.display = "none";
        }
    });
    
    // Simulación de carga inicial con ejemplo realista
    window.addEventListener("load", () => {
        // Extraer simulación de "web" - dejamos datos precargados
        console.log("Aplicación cargada: datos de medicamentos simulados desde base de conocimiento veterinario.");
        // Pre-cálculo para mostrar valores por defecto (Border Collie, 10kg)
        const especieDef = "perro";
        const pesoDef = 10;
        const edadDef = "adulto";
        const estadoDef = "neutro";
        const razaDef = "Border Collie";
        const esMDR1 = checkMDR1(razaDef);
        document.getElementById("razaWarning").style.display = esMDR1 ? "inline-block" : "none";
        renderResults(especieDef, pesoDef, edadDef, estadoDef, razaDef, esMDR1);
    });
</script>
</body>
</html>
