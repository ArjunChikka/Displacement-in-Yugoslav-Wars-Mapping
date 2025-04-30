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
            "On June 25, 1991, Croatia and Slovenia officially declared independence from the Socialist Federal Republic of Yugoslavia, sparking immediate tensions. "
            "While Slovenia fought a short conflict and quickly secured its autonomy, Croatia plunged into a brutal war. "
            "Ethnic Serb populations within Croatia, armed by the Yugoslav People's Army (JNA) and nationalist paramilitaries, refused to recognize the new Croatian state. "
            "Skirmishes escalated into full-scale battles as villages across Krajina and Slavonia became engulfed in violence. "
            "The initial displacements began, with both Croat and Serb civilians fleeing areas of ethnic tension."
        ),

        html.H5("July–August 1991 — JNA Intervention and Full-Scale War"),
        html.P(
            "During the summer months of 1991, the Yugoslav People's Army launched a coordinated intervention across Croatian territory. "
            "Cities such as Osijek, Dubrovnik, and Karlovac faced heavy artillery shelling and tank offensives, devastating urban centers and historic landmarks. "
            "Mass civilian displacement followed as Croatian populations fled Serb-occupied towns, while ethnic Serbs fled Croat-held areas in fear of reprisals. "
            "The humanitarian situation rapidly deteriorated, with makeshift refugee camps emerging across Croatia and neighboring countries. "
            "Efforts by the European Community to mediate the conflict largely failed, and full-scale war appeared inevitable."
        ),

        html.H5("August 25, 1991 — Beginning of the Siege of Vukovar"),
        html.P(
            "On August 25, 1991, the multiethnic city of Vukovar came under siege by Serb forces in what would become one of the most infamous battles of the Croatian War. "
            "For 87 days, Vukovar's defenders, including both soldiers and civilians, endured relentless shelling, sniper attacks, and supply blockades. "
            "Medical facilities collapsed under the strain, with surgeries performed by flashlight and patients dying for lack of basic supplies. "
            "Tens of thousands of civilians sought refuge in basements, surviving on dwindling food supplies. "
            "The siege symbolized both Croatian resistance and the extreme suffering faced by civilians trapped by war."
        ),

        html.H5("November 18, 1991 — Fall of Vukovar and Ovčara Massacre"),
        html.P(
            "After months of heroic resistance, Vukovar fell to Serb forces, leading to one of the war’s worst atrocities. "
            "At Ovčara farm, approximately 260 wounded prisoners and civilians were executed and buried in mass graves. "
            "Thousands more were forcibly expelled from the region, their homes looted and torched. "
            "News of the massacre shocked international audiences but failed to provoke direct intervention. "
            "Vukovar’s destruction became a grim icon of the human cost of Yugoslavia’s collapse."
        ),

        html.H5("December 1991–January 1992 — Ethnic Cleansing and UN Intervention"),
        html.P(
            "In the aftermath of Vukovar, ethnic cleansing campaigns intensified across Serb-controlled areas, particularly in Krajina and Eastern Slavonia. "
            "Croat civilians were forcibly evicted, and Serb militias destroyed entire villages to erase Croatian cultural presence. "
            "International pressure mounted, culminating in the UN-brokered Sarajevo Agreement in early 1992. "
            "United Nations Protection Forces (UNPROFOR) were deployed to maintain ceasefire lines, but they lacked the mandate to reverse ethnic cleansing. "
            "By winter's end, over half a million Croatians remained displaced inside and outside of Croatia."
        ),
    ]),

    "1992–1995": html.Div([
        html.H4("Expanded Timeline: Bosnian War (1992–1995)"),

        html.H5("March 1, 1992 — Bosnia's Independence Referendum and Descent into War"),
        html.P(
            "Bosnia and Herzegovina’s independence referendum, held on March 1, 1992, passed overwhelmingly despite a boycott by most Bosnian Serbs. "
            "Immediately afterward, Bosnian Serb forces, with heavy support from the Yugoslav Army, launched attacks to seize territory for an envisioned Serb state. "
            "Sarajevo descended into chaos, with snipers firing on civilians and ethnic enclaves solidifying within neighborhoods. "
            "Tensions that had simmered for months erupted into open violence as communities splintered along ethnic lines. "
            "Within weeks, tens of thousands of civilians had been displaced, and the conflict expanded rapidly."
        ),

        html.H5("April 1992 — Siege of Sarajevo"),
        html.P(
            "In April 1992, Serb forces encircled Sarajevo, initiating what would become the longest siege in modern history, lasting nearly four years. "
            "Artillery, mortars, and snipers rained terror upon the city’s trapped population, killing civilians indiscriminately. "
            "Water, electricity, and medical supplies became luxuries, and families lived in basements for months at a time. "
            "Aid convoys struggled to penetrate the blockade, and black markets flourished as desperation took hold. "
            "Sarajevo’s ordeal epitomized the civilian suffering that characterized the Bosnian War."
        ),

        html.H5("May–August 1992 — Ethnic Cleansing in Eastern Bosnia"),
        html.P(
            "Throughout the summer of 1992, Serb forces systematically cleansed eastern Bosnia of its Bosniak and Croat populations. "
            "Towns like Višegrad, Foča, and Prijedor witnessed mass executions, sexual violence, and the establishment of infamous detention camps. "
            "Men and boys disappeared into camps where torture and murder were routine, while women faced sexual slavery. "
            "Entire communities were obliterated, their mosques and homes reduced to rubble. "
            "International observers documented the atrocities, but effective intervention remained elusive."
        ),

        html.H5("1993–1994 — UN 'Safe Areas' and Humanitarian Failures"),
        html.P(
            "Facing mounting evidence of ethnic cleansing, the UN established 'safe areas' intended to shelter civilians from attack. "
            "However, these enclaves, such as Srebrenica and Goražde, were under-supplied and weakly defended. "
            "Instead of protecting civilians, the zones often served as targets for further aggression. "
            "Aid deliveries were sporadic, and living conditions in the enclaves deteriorated into near-famine conditions. "
            "International credibility suffered as promises of protection repeatedly proved hollow."
        ),

        html.H5("July 1995 — Fall of Srebrenica"),
        html.P(
            "In July 1995, Serb forces overran the UN-protected town of Srebrenica, committing the single worst atrocity of the Bosnian War. "
            "Over 8,000 Bosniak men and boys were executed in mass killings organized with chilling efficiency. "
            "Women and children were forcibly deported, while Dutch peacekeepers stationed in the town stood by, powerless. "
            "The massacre shocked the world and provided irrefutable evidence of genocide. "
            "It would become the subject of international war crimes prosecutions and memorials for decades to come."
        ),

        html.H5("August–December 1995 — NATO Intervention and Dayton Agreement"),
        html.P(
            "Following the horror of Srebrenica and renewed shelling of Sarajevo, NATO launched Operation Deliberate Force. "
            "Relentless airstrikes crippled Serb military infrastructure, shifting the balance of power. "
            "Croatian military offensives further pressured Serb forces on the ground. "
            "Peace talks held at Wright-Patterson Air Force Base in Dayton, Ohio, brokered a fragile peace agreement. "
            "While the Dayton Accords ended active fighting, they cemented ethnic divisions and left millions displaced from their former homes."
        ),
    ]),

    "1998–1999": html.Div([
        html.H4("Expanded Timeline: Kosovo War (1998–1999)"),

        html.H5("February 28, 1998 — Kosovo Liberation Army (KLA) Attacks Spark Crackdown"),
        html.P(
            "On February 28, 1998, the Kosovo Liberation Army (KLA) launched attacks against Serbian police forces in Kosovo, demanding independence for Kosovo’s ethnic Albanian majority. "
            "In response, Serbian authorities began widespread retaliatory operations, targeting not just militants but entire villages. "
            "Civilians were subjected to massacres, forced evictions, and systematic destruction of property. "
            "Many fled into forests, surviving in precarious conditions as international observers documented growing abuses. "
            "Despite mounting evidence, diplomatic efforts to prevent a broader conflict repeatedly stalled."
        ),

        html.H5("Summer–Fall 1998 — Mass Displacement in the Drenica Valley"),
        html.P(
            "Throughout the summer and fall of 1998, Serbian offensives devastated ethnic Albanian strongholds, particularly in the Drenica Valley. "
            "Villages were razed, civilians fled en masse, and humanitarian access was severely restricted. "
            "Families endured months in makeshift camps without reliable food, water, or medical care. "
            "Journalists and human rights groups highlighted the humanitarian catastrophe, but international military action remained elusive. "
            "As winter approached, hundreds of thousands faced starvation and exposure."
        ),

        html.H5("January 15, 1999 — Račak Massacre"),
        html.P(
            "The discovery of 45 Albanian civilians executed at Račak on January 15, 1999, served as a turning point in the Kosovo conflict. "
            "Western monitors, including William Walker of the OSCE, declared the killings a massacre, igniting global outrage. "
            "Serbian authorities denied wrongdoing, insisting the dead were KLA fighters, but forensic evidence contradicted these claims. "
            "The Račak Massacre shattered any remaining hopes for negotiated peace. "
            "Talks at Rambouillet soon collapsed, paving the way for NATO intervention."
        ),

        html.H5("March 24, 1999 — NATO Bombing Campaign"),
        html.P(
            "NATO launched an air campaign against Yugoslavia on March 24, 1999, aimed at halting Serbian atrocities in Kosovo. "
            "In retaliation, Serbian forces intensified ethnic cleansing efforts, expelling nearly a million Albanians within weeks. "
            "Entire villages were burned, civilians were separated and executed, and refugees crowded into overloaded camps in Albania and Macedonia. "
            "The sheer scale of human suffering galvanized world opinion. "
            "Despite criticisms of collateral damage, NATO remained resolute, extending the bombing campaign for 78 days."
        ),

        html.H5("June 1999 — Serbian Withdrawal and Humanitarian Aftermath"),
        html.P(
            "On June 10, 1999, after weeks of relentless NATO airstrikes and growing political pressure, Serbian forces agreed to withdraw from Kosovo. "
            "NATO-led KFOR troops moved in to stabilize the region and facilitate the return of hundreds of thousands of Albanian refugees. "
            "Returning families found their villages destroyed and their homes looted. "
            "Meanwhile, revenge attacks by Albanians against Serbs and Roma triggered a new wave of displacement. "
            "Though Kosovo would declare independence in 2008, ethnic tensions and unresolved grievances continue to haunt the region today."
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
    app.run_server(debug=False, host="0.0.0.0", port=10000)

#if __name__ == "__main__":
#    app.run(debug=True)

