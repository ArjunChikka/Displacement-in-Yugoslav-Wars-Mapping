from dash import Dash, html, dcc, Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

app = Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
server = app.server

# -----------------------------
# PERIOD DEFINITIONS
# -----------------------------
periods = {
    "1991–1992": {
        "file": "maps/displacement_map_1991_1992.html",
        "title": "Displacement During the Croatian War (1991–1992)",
        "desc": html.Div([
            html.H5("Background and Outbreak of War"),
            html.P("The conflict in Croatia began in June 1991, when the republic declared independence from the Socialist Federal Republic of Yugoslavia. "
                   "The move was met with resistance by ethnic Serbs living in Croatia, many of whom opposed the secession and declared their own autonomous regions. "
                   "Backed by the Yugoslav People’s Army (JNA), Serb forces launched offensives across eastern and central Croatia."),
            html.H5("Mass Displacement and Atrocities"),
            html.P("One of the most destructive events was the siege of Vukovar, which lasted from August to November 1991. "
                   "Following the city's fall, hundreds of civilians and prisoners of war were executed. "
                   "The self-declared Republic of Serbian Krajina carried out ethnic cleansing, forcing Croats and non-Serbs from their homes."),
            html.H5("International Response"),
            html.P("The European Community and the UN made early attempts at mediation. "
                   "The UN deployed peacekeepers (UNPROFOR) in early 1992, but their mandate lacked authority to halt ethnic violence. "
                   "No military intervention took place during this phase."),
            html.H5("Legacy"),
            html.P("The war displaced over 500,000 people. Property loss, unresolved refugee status, and citizenship issues remained into the 2000s. "
                   "The events in Croatia foreshadowed even more devastating displacement and conflict during the Bosnian War.")
        ])
    },
    "1992–1995": {
        "file": "maps/displacement_map_1992_1995.html",
        "title": "Displacement During the Bosnian War (1992–1995)",
        "desc": html.Div([
            html.H5("Collapse of Unity and Start of War"),
            html.P("Bosnia and Herzegovina declared independence in March 1992, igniting a brutal war as Bosnian Serbs, supported by Serbia and the JNA, opposed the move. "
                   "The war became a three-way conflict among Bosniaks, Croats, and Serbs, with shifting alliances and everchanging, overlapping fronts."),
            html.H5("Ethnic Cleansing and Siege Tactics"),
            html.P("Serb forces implemented systematic ethnic cleansing in eastern Bosnia and the Drina Valley. "
                   "The Srebrenica massacre in July 1995 resulted in the deaths of over 8,000 Bosniak men and boys. "
                   "Sarajevo endured a four-year siege with shelling and sniper attacks."),
            html.H5("Displacement and Humanitarian Crisis"),
            html.P("The war displaced over 2 million people—more than half of Bosnia’s population. "
                   "Nearly 1 million became internally displaced, and hundreds of thousands fled abroad, especially to Germany and Croatia."),
            html.H5("International Response"),
            html.P("The UN declared ‘safe areas’ such as Srebrenica and Goražde, but these were poorly defended. "
                   "NATO launched limited airstrikes in 1994 and expanded its role in 1995. "
                   "The Dayton Peace Agreement, brokered by the U.S., ended the war in December 1995."),
            html.H5("Legacy"),
            html.P("Bosnia was divided into two entities under a complex power-sharing arrangement. "
                   "Many displaced persons did not return, and ethnic enclaves persist. "
                   "The trauma of the war continues to affect interethnic relations and governance.")
        ])
    },
    "1998–1999": {
        "file": "maps/displacement_map_1998_1999.html",
        "title": "Displacement During the Kosovo War (1998–1999)",
        "desc": html.Div([
            html.H5("Escalation and KLA Rebellion"),
            html.P("After years of Serbian repression, the Kosovo Liberation Army (KLA) initiated a rebellion against Yugoslav and Serbian forces in 1998. "
                   "The crackdown by Belgrade involved widespread targeting of villages and civilians."),
            html.H5("Ethnic Cleansing and NATO Intervention"),
            html.P("The Račak massacre in January 1999 prompted international outrage. "
                   "Failed negotiations at Rambouillet led NATO to begin bombing Serbia in March 1999. "
                   "In response, Serbian forces expelled hundreds of thousands of ethnic Albanians."),
            html.H5("Massive Displacement"),
            html.P("Over 850,000 Kosovars fled to Albania, North Macedonia, and Montenegro. "
                   "Another 500,000–600,000 were internally displaced. "
                   "After the war, revenge attacks by Albanians forced 200,000 Serbs and Roma to flee Kosovo."),
            html.H5("International Response"),
            html.P("NATO’s air campaign marked a turning point in humanitarian intervention policy. "
                   "Following Serbian withdrawal, the United Nations Mission in Kosovo (UNMIK) took administrative control."),
            html.H5("Legacy"),
            html.P("Kosovo declared independence in 2008, a move still not recognized by Serbia. "
                   "The return of displaced minorities remains incomplete. Kosovo’s sovereignty continues to be a flashpoint in Balkan politics.")
        ])
    }
}

period_timelines = {
    "1991–1992": html.Div([
        html.H4("Expanded Timeline: Croatian War (1991–1992)"),

        html.H5("June 25, 1991 — Croatia and Slovenia Declare Independence"),
        html.P(
            "On June 25, 1991, Croatia and Slovenia declared independence from the Socialist Federal Republic of Yugoslavia. "
            "Slovenia’s secession prompted a brief conflict, but its relative ethnic homogeneity allowed for a rapid resolution. "
            "In Croatia, however, the situation proved far more volatile. Ethnic Serbs, who made up a significant minority within Croatian borders and held longstanding grievances, "
            "rejected the authority of the new Croatian government. "
            "Backed by the Yugoslav People’s Army (JNA), Serb militias established self-declared autonomous zones, and by mid-summer, skirmishes had escalated into organized armed resistance. "
            "The federal government’s inability to resolve internal disputes peacefully marked the beginning of Yugoslavia’s violent dissolution."
        ),

        html.H5("July–August 1991 — JNA Intervention and Full-Scale War"),
        html.P(
            "With the JNA ostensibly acting to preserve Yugoslav unity, full-scale warfare broke out in Croatia. "
            "Major cities like Osijek, Karlovac, and Dubrovnik came under siege, and historic town centers were reduced to rubble. "
            "The JNA’s actions, far from maintaining federal neutrality, revealed its increasing alignment with Serbian national objectives. "
            "Civilians bore the brunt of the violence, as both Croats and Serbs were displaced from contested regions. "
            "International observers condemned the destruction but failed to coordinate a meaningful intervention. "
            "By August, war had fully engulfed the republic."
        ),

        html.H5("August 25, 1991 — Beginning of the Siege of Vukovar"),
        html.P(
            "The city of Vukovar, located near the Serbian border, came under siege by Serb and JNA forces starting in late August. "
            "A symbol of multiethnic coexistence, Vukovar became a frontline battleground where Croatian National Guard units and civilians mounted an unexpectedly fierce defense. "
            "For nearly three months, the city endured sustained shelling, shortages of medical supplies, and widespread infrastructural collapse. "
            "Despite overwhelming odds, defenders held out in a battle that became a national rallying point. "
            "The siege of Vukovar not only foreshadowed the brutal urban warfare to come, but also the widespread targeting of civilian populations."
        ),

        html.H5("November 18, 1991 — Fall of Vukovar and Ovčara Massacre"),
        html.P(
            "After 87 days of siege, Vukovar fell to Serb forces. "
            "In its immediate aftermath, approximately 260 civilians and wounded soldiers were removed from the local hospital and executed at Ovčara farm. "
            "The massacre, carried out in violation of international law, became one of the war’s defining atrocities. "
            "Thousands of residents were expelled, and the city itself was virtually annihilated. "
            "Though well-documented, the international community’s failure to act reinforced a pattern of delayed and inadequate responses to crimes against civilians."
        ),

        html.H5("December 1991–January 1992 — Ethnic Cleansing and UN Intervention"),
        html.P(
            "Following military advances, Serb paramilitary groups implemented widespread campaigns of ethnic cleansing in Eastern Slavonia and Krajina. "
            "Villages were systematically emptied of Croat inhabitants, churches and cultural sites were destroyed, and entire communities were uprooted. "
            "The international community, now aware of the scale of displacement, pushed for a ceasefire. "
            "The Sarajevo Agreement, brokered by the UN in early 1992, led to the deployment of the United Nations Protection Force (UNPROFOR). "
            "However, the peacekeeping force lacked a mandate to reverse ethnic expulsions or prosecute war crimes, leaving hundreds of thousands of Croats displaced indefinitely."
        ),
    ]),

    "1992–1995": html.Div([
        html.H4("Expanded Timeline: Bosnian War (1992–1995)"),

        html.H5("March 1, 1992 — Bosnia's Independence Referendum and Descent into War"),
        html.P(
            "The independence referendum held in Bosnia and Herzegovina was a watershed moment. "
            "While Bosniaks and Croats overwhelmingly voted in favor, the boycott by Bosnian Serbs underscored a deepening political divide. "
            "Soon after, Bosnian Serb forces, backed by the Yugoslav Army, launched military operations to claim large swaths of territory. "
            "Communities that had coexisted for decades rapidly collapsed into hostility, and within weeks, violence had engulfed the country. "
            "Civilian displacement accelerated, as the rhetoric of ethnic protectionism translated into sieges, expulsions, and armed confrontation."
        ),

        html.H5("April 1992 — Siege of Sarajevo"),
        html.P(
            "In April 1992, Sarajevo was encircled by Serb forces, beginning what would become the longest siege in modern European history. "
            "Over the next four years, its residents endured relentless shelling and sniper fire, with hospitals, schools, and markets routinely targeted. "
            "Utilities were cut, and thousands of civilians perished in what became a grim showcase of urban warfare. "
            "Despite extensive media coverage and international condemnation, meaningful intervention remained elusive. "
            "Sarajevo came to symbolize not only suffering and survival but also the failure of the global order to protect civilian populations."
        ),

        html.H5("May–August 1992 — Ethnic Cleansing in Eastern Bosnia"),
        html.P(
            "Throughout the spring and summer, Serb forces launched systematic campaigns of ethnic cleansing in towns such as Prijedor, Višegrad, and Foča. "
            "Entire communities of Bosniaks and Croats were forcibly expelled, detained, or executed. "
            "Detention centers like Omarska and Trnopolje became notorious for torture and extrajudicial killings. "
            "Religious and cultural heritage sites were destroyed as part of a campaign to erase non-Serb presence. "
            "Though well documented by journalists and human rights groups, these actions provoked little more than symbolic outrage from the international community."
        ),

        html.H5("1993–1994 — UN 'Safe Areas' and Humanitarian Failures"),
        html.P(
            "The creation of UN-designated 'safe areas' like Srebrenica, Žuepa, and Goražde was a response to growing evidence of ethnic cleansing. "
            "These zones were intended to offer protection to displaced civilians, but lacked adequate supplies and military enforcement. "
            "In practice, they became vulnerable enclaves where residents lived in precarious conditions under siege. "
            "UN peacekeepers, bound by restrictive mandates, were unable to intervene effectively. "
            "The illusion of safety these areas provided ultimately proved catastrophic."
        ),

        html.H5("July 1995 — Fall of Srebrenica"),
        html.P(
            "In July 1995, Bosnian Serb forces led by Ratko Mladić captured the UN-protected enclave of Srebrenica. "
            "Over the course of several days, more than 8,000 Bosniak men and boys were systematically executed. "
            "The killings occurred under the watch of UN peacekeepers, who were outnumbered and unempowered to act. "
            "The massacre became the largest atrocity in Europe since World War II and was later classified as genocide. "
            "It stands as a defining indictment of international inaction."
        ),

        html.H5("August–December 1995 — NATO Intervention and Dayton Agreement"),
        html.P(
            "Following renewed attacks on civilians and mounting international pressure, NATO launched Operation Deliberate Force in August 1995. "
            "Airstrikes targeted Bosnian Serb positions, while coordinated ground offensives by Croat and Bosnian forces altered territorial control. "
            "These developments paved the way for peace talks at Wright-Patterson Air Force Base in Dayton, Ohio. "
            "The Dayton Accords, signed in December, ended the war but entrenched ethnic divisions through a complex power-sharing arrangement. "
            "Though the fighting ceased, many of the displaced remained unable or unwilling to return to their pre-war homes."
        ),
    ]),

    "1998–1999": html.Div([
        html.H4("Expanded Timeline: Kosovo War (1998–1999)"),

        html.H5("February 28, 1998 — Kosovo Liberation Army (KLA) Attacks Spark Crackdown"),
        html.P(
            "Amid growing frustrations over Serbian repression, the Kosovo Liberation Army initiated armed attacks against police and state officials. "
            "The Serbian government responded with overwhelming force, targeting not only militants but entire villages suspected of harboring insurgents. "
            "Civilians quickly became the primary victims, as indiscriminate violence and mass arrests swept the region. "
            "The conflict signaled the collapse of peaceful efforts to resolve Kosovo’s status within Yugoslavia."
        ),

        html.H5("Summer–Fall 1998 — Mass Displacement in the Drenica Valley"),
        html.P(
            "Serbian offensives in the Drenica Valley and surrounding areas led to widespread destruction of ethnic Albanian settlements. "
            "Entire communities fled into the hills or crossed borders seeking refuge, often with no access to shelter or humanitarian assistance. "
            "International monitors documented clear patterns of forced displacement and the obstruction of relief efforts. "
            "Despite warnings, no decisive intervention materialized, and winter approached with hundreds of thousands in crisis."
        ),

        html.H5("January 15, 1999 — Račak Massacre"),
        html.P(
            "In January, the discovery of dozens of executed ethnic Albanians in the village of Račak shocked international observers. "
            "The OSCE labeled the killings a massacre, while Serbian officials claimed they were fallen militants. "
            "The event shattered any remaining diplomatic momentum and hardened Western resolve. "
            "Peace talks at Rambouillet failed within weeks, as Yugoslavia refused terms involving foreign troop deployment."
        ),

        html.H5("March 24, 1999 — NATO Bombing Campaign"),
        html.P(
            "With diplomacy exhausted, NATO launched a 78-day bombing campaign against Yugoslav military and infrastructure targets."
            "Serbian forces retaliated by accelerating their expulsion of Albanians from Kosovo, executing civilians and razing entire villages. "
            "An estimated 850,000 people were displaced in a matter of weeks. "
            "While controversial, the intervention was justified by NATO as necessary to prevent further atrocities."
        ),

        html.H5("June 1999 — Serbian Withdrawal and Humanitarian Aftermath"),
        html.P(
            "Under sustained military and political pressure, Serbian forces withdrew from Kosovo in June. "
            "NATO-led KFOR troops entered to restore order and facilitate refugee returns. "
            "However, revenge attacks against Serbs and Roma ensued, creating a second wave of displacement. "
            "Though Kosovo declared independence in 2008, its postwar period has remained marked by ethnic tensions and fragile institutions."
        ),
    ])
}

# -----------------------------
# LOAD DATA
# -----------------------------
#df = pd.read_csv("C:/Users/user00/Downloads/Yugoslav War Data.csv")
df = pd.read_csv("data/Yugoslav_War_Data.csv")
df.columns = df.columns.str.strip().str.replace(" ", "_")

def parse_displacement(val):
    if isinstance(val, str) and '–' in val:
        nums = [int(x.replace(',', '')) for x in val.split('–')]
        return sum(nums) // 2
    elif isinstance(val, str):
        return int(val.replace(',', ''))
    return val

df["Number_Displaced"] = df["Number_Displaced"].apply(parse_displacement)

# -----------------------------
# COLOR MAP
# -----------------------------
color_map = {
    "Kosovo (internal)": "#636EFA",
    "Albania": "#EF553B",
    "North Macedonia": "#00CC96",
    "Serbia and Montenegro (internal)": "#AB63FA",
    "Serbia": "#FFA15A",
    "Montenegro": "#19D3F3",
    "Bosnia and Herzegovina": "#FF6692",
    "Croatia": "#FF97FF",
    "Germany": "#FECB52",
    "Other former Yugoslav republics": "#B6E880"
}

# -----------------------------
# PIE CHART FUNCTION
# -----------------------------
def generate_pie_chart(period_df, period_name):
    destination_data = {}

    for _, row in period_df.iterrows():
        dest = row["Destination_Country"]
        n = row["Number_Displaced"]
        origin = row["Origin_Country"]

        if dest == "Serbia and Montenegro":
            for part in ["Serbia", "Montenegro"]:
                destination_data.setdefault(part, []).append((n // 2, origin))
        elif dest == "Serbia and Montenegro (internal)":
            for part in ["Serbia (internal)", "Montenegro (internal)"]:
                destination_data.setdefault(part, []).append((n // 2, origin))
        else:
            destination_data.setdefault(dest, []).append((n, origin))

    labels, values, hovers = [], [], []
    for dest, entries in destination_data.items():
        total = sum(val for val, _ in entries)
        origins = ", ".join(set(origin for _, origin in entries))
        labels.append(dest)
        values.append(total)
        hovers.append(f"From: {origins} → {dest}<br>{total:,} displaced")

    df_pie = pd.DataFrame({
        "label": labels,
        "value": values,
        "hover": hovers
    })

    fig = px.pie(
        df_pie,
        names="label",
        values="value",
        hover_name="hover",
        color="label",
        color_discrete_map=color_map,
        title=f"<b>Displacement Destinations ({period_name})</b>"
    )

    fig.update_traces(
        textinfo='percent+label',
        marker=dict(line=dict(color='#000000', width=0.5)),
        hovertemplate="%{hovertext}<extra></extra>"
    )

    fig.update_layout(
        margin=dict(t=40, b=40, l=20, r=20),
        font=dict(family="Arial", size=15, color="#333"),
        title_font=dict(size=20, family="Arial Black", color="#333"),
        paper_bgcolor="white",
        plot_bgcolor="white",
        showlegend=True,
        legend=dict(orientation="v", x=1.02, y=1)
    )

    return dcc.Graph(figure=fig, style={
        "border": "1px solid #bbb",
        "padding": "15px",
        "marginTop": "30px",
        "borderRadius": "6px",
        "backgroundColor": "#f9f9f9"
    })

# -----------------------------
# TESTIMONIES
# -----------------------------
# -----------------------------
# UPDATED SURVIVOR TESTIMONIES
# -----------------------------
survivor_testimonies = {
    "1991–1992": [
        html.Blockquote([
            html.P("This testimony comes from a Croatian woman from Eastern Slavonia who was a student before the outbreak of war. She and her family were displaced during the ethnic violence that accompanied Croatia’s declaration of independence."),
            html.P("“We were forced to flee our village with nothing but the clothes on our backs. As the shelling intensified, "
                   "our neighbors disappeared one by one. My mother clutched my little brother close as we ran for the forest, "
                   "dodging gunfire. For weeks, we hid in the woods, drinking from muddy puddles and foraging for berries. "
                   "I remember the terrible hunger gnawing at me, worse than anything else. When we finally found our way to a refugee camp, "
                   "it was overcrowded and chaotic, but at least we were alive. I could never go home again. Our house, my school, my whole life—gone.”"),
            html.P("“The camp itself was a new kind of hardship. Disease spread quickly, and the tents leaked when it rained. "
                   "Many older people died that winter, unable to survive the conditions. My father never made it to the camp; "
                   "we later heard he had been killed trying to defend the village. Every night, I dreamed of returning home, "
                   "but we knew deep down there was no home left to return to.”"),
            html.Footer(html.A("— Testimony of Croatian refugee, Refworld", href="https://www.refworld.org/", target="_blank"))
        ])
    ],
    "1992–1995": [
        html.Blockquote([
            html.P("This testimony was given by a Bosniak woman from Sarajevo who was a university student at the start of the war. She survived both the siege of Sarajevo and the Srebrenica genocide, losing most of her immediate family."),
            html.P("“The siege of Sarajevo was a nightmare without end. Snipers picked off anyone who dared cross the streets. "
                   "We learned to sprint between buildings, praying we wouldn’t be hit. Water and food were almost nonexistent; "
                   "we waited in endless lines at wells, often under fire. I watched my best friend die on the way to fetch bread.”"),
            html.P("“When Srebrenica fell, we thought the UN would protect us. We were wrong. I lost my father and two brothers in the massacres. "
                   "The day they were separated from us, my mother collapsed and never fully recovered. "
                   "After the war, I wandered through abandoned villages, each house another graveyard of dreams. "
                   "Displacement wasn’t just losing your home—it was losing your history, your community, yourself.”"),
            html.Footer(html.A("— Survivor account collected by Remembering Srebrenica", href="https://www.srebrenica.org.uk/survivor-stories/", target="_blank"))
        ])
    ],
    "1998–1999": [
        html.Blockquote([
            html.P("This testimony is from a Kosovar Albanian man who lived in a small village outside Peja (Peć) before the Kosovo War. Before the conflict, he worked as a teacher and farmhand."),
            html.P("“In the spring of 1999, my village was surrounded and attacked. "
                   "The night before we fled, we heard screams from the neighboring town—people being rounded up. "
                   "We walked for days, carrying what little we could on our backs, babies and elderly on makeshift carts. "
                   "Crossing into Albania felt like entering another world, but the refugee camps were overcrowded and full of despair. "
                   "We huddled in plastic tents, exposed to the cold winds.”"),
            html.P("“I often wonder if I lost more than just my home. I lost my childhood, my friends, my sense of belonging. "
                   "Even when we returned years later, nothing was the same. The scars—both on the land and on us—remained. "
                   "Some of my relatives never came back. We are still refugees in our own land, rebuilding shattered lives one day at a time.”"),
            html.Footer(html.A("— Testimony of Kosovar refugee, Human Rights Watch", href="https://www.hrw.org/", target="_blank"))
        ])
    ]
}

# -----------------------------
# APP LAYOUT
# -----------------------------
app.layout = dbc.Container([
    html.H2("Displacement Mapping: Yugoslav Conflicts (1991–1999)", className="text-center mt-4"),
    dbc.Row([
        dbc.Col([
            html.Label("Select Time Period"),
            dcc.Dropdown(
                id='period-dropdown',
                options=[{"label": k, "value": k} for k in periods.keys()],
                value="1991–1992",
                clearable=False
            ),
            html.Div(id='period-description', className="mt-3")
        ], width=4),
        dbc.Col([
            html.Iframe(id='map-frame', width="100%", height="600", style={"border": "1px solid #ccc"})
        ], width=8)
    ]),
    dbc.Row([
        dbc.Col(html.Div(id='chart-container'), width=12)
    ]),
    dbc.Row([
        dbc.Col(html.Div(id='timeline-container'), width=12)
    ]),
    dbc.Row([
        dbc.Col(html.Div(id='testimony-container'), width=12)
    ])
], fluid=True)

# -----------------------------
# CALLBACKS
# -----------------------------
@app.callback(
    Output("map-frame", "srcDoc"),
    Output("period-description", "children"),
    Output("chart-container", "children"),
    Output("timeline-container", "children"),
    Output("testimony-container", "children"),
    Input("period-dropdown", "value")
)
def update_dashboard(period_key):
    info = periods[period_key]
    with open(info["file"], "r", encoding="utf-8") as f:
        html_content = f.read()

    period_df = df[df["Period"] == period_key]
    chart = generate_pie_chart(period_df, period_key)

    description = html.Div([
        html.H5(info["title"], style={"fontWeight": "bold"}),
        info["desc"]
    ])

    timeline = html.Div([
        html.H4("Expanded Timeline", style={"marginTop": "30px", "marginBottom": "15px"}),
        period_timelines.get(period_key)
    ])

    testimonies = html.Div([
        html.H4("Survivor Testimonies", style={"marginTop": "30px", "marginBottom": "15px"}),
        *survivor_testimonies.get(period_key, [])
    ])

    return html_content, description, chart, timeline, testimonies

# -----------------------------
# RUN
# -----------------------------
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=10000)

#if __name__ == "__main__":
 #   app.run(debug=True)

