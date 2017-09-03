# other script
import graph_randomiser as gr 
import gs_data as gsd

sim = gsd.full_sim_for_family('random_scale_free', gr.random_scale_free_graph, [1000, 2], 5, 5)
gsd.save_sim_data(sim)



reds_line = plt.plot(map(lambda g : g.graph['energy'], REDS_list_s05), map(lambda g : g.size(), REDS_list_s05), 'b-', label = 'REDS')
rgg_line = plt.plot(map(lambda g : g.graph['energy'], RGG_list), map(lambda g : g.size(), RGG_list), 'g-', label = 'RGG')
four_line = plt.plot(map(lambda g : g.graph['energy'], RGG_list), [4000 for x in range(20)], 'r-', label = '4000')
plt.xlabel('energy')
plt.ylabel('size')
plt.legend()
plt.title('Graph Size against Energy for S=0.5 REDS Networks. Converges to RGG network as Energy increases.')
plt.show()


figure(num=None, figsize=(8, 6), dpi=80, facecolor='w', edgecolor='k')


range1 = reds_range()
range1_df = pd.DataFrame(range1)
f = open(data_directory+'REDSrange1\\graph_df.redsgraph', 'w')
pickle.dump(range1_df, f)
f.close()


reds_sim = gsd.full_sim_for_family('REDS', rc.reds_graph, [1000, 0.1, 0.15, 1.0], 5, 5, 1e4, 1e3)
gsd.save_sim_data(reds_sim)


cProfile.run('full_sim(G, 1.6, 1e3, 1e2)', sort='tottime')


graph_dict = setup_graph_dict()
compare_degree_distribution_plot(graph_dict)

# Mockup
import reds_construct as rc
import gs_data as gsd
import gs_analysis as gsa
import networkx as nx
import matplotlib.pyplot as plt

erdos_sim = gsd.full_sim_for_family('erdos_renyi', nx.watts_strogatz_graph, [1000, 10, 1], 5, 5, 1e4, 1e3)
gsa.full_analysis(erdos_sim)
gsd.save_sim_data(erdos_sim)

barabasi_sim = gsd.full_sim_for_family('barabasi_albert', nx.barabasi_albert_graph, [1000, 5], 5, 5, 1e4, 1e3)
gsa.full_analysis(barabasi_sim)
gsd.save_sim_data(barabasi_sim)

rsf_sim = gsd.full_sim_for_family('random_scale_free', gr.random_scale_free_graph, [1000, 5], 5, 5, 1e4, 1e3)
gsa.full_analysis(rsf_sim)
gsd.save_sim_data(rsf_sim)

reds_sim = gsd.full_sim_for_family('reds', rc.reds_graph, [1000, 0.1, 0.146, 1.0], 5, 5, 1e4, 1e3)
gsa.full_analysis(reds_sim)
gsd.save_sim_data(reds_sim)

rgg_sim = gsd.full_sim_for_family('rgg', rc.RGG_md_graph, [1000, 10], 5, 5, 1e4, 1e3)
gsa.full_analysis(rgg_sim)
gsd.save_sim_data(rgg_sim)

sw_reds_sim = gsd.full_sim_for_family('smallworld_reds', rc.small_world_reds_graph, [1000, 0.1, 0.146, 1.0, 0.2], 5, 5, 1e4, 1e3)
gsa.full_analysis(sw_reds_sim)
gsd.save_sim_data(sw_reds_sim)

regular_sim = gsd.full_sim_for_family('regular', nx.watts_strogatz_graph, [1000, 10, 0], 5, 5, 1e4, 1e3)
gsa.full_analysis(regular_sim)
gsd.save_sim_data(regular_sim)

comm_rand_reds_sim = gsd.full_sim_for_family('comm_rand_reds', rc.small_world_reds_graph, [1000, 0.1, 0.146, 1.0, 1.0], 5, 5, 1e4, 1e3)
gsa.full_analysis(comm_rand_reds_sim)
gsd.save_sim_data(comm_rand_reds_sim)


comm_reds_sim = gsd.full_sim_for_family('comm_reds', rc.reds_graph, [1000, 0.1, 0.146, 1.0], 5, 5, 1e4, 1e3, comm_init=True)
gsa.full_analysis(comm_reds_sim)
gsd.save_sim_data(comm_reds_sim)


comm_erdos_sim = gsd.full_sim_for_family('comm_erdos_renyi', nx.watts_strogatz_graph, [1000, 10, 1], 5, 5, 1e4, 1e3, comm_init=True)
gsa.full_analysis(comm_erdos_sim)
gsd.save_sim_data(comm_erdos_sim)

comm_barabasi_sim = gsd.full_sim_for_family('comm_barabasi_albert', nx.barabasi_albert_graph, [1000, 5], 5, 5, 1e4, 1e3, comm_init=True)
gsa.full_analysis(comm_barabasi_sim)
gsd.save_sim_data(comm_barabasi_sim)

sim_dict1 = {'Regular': regular_sim, 'Erdos-Renyi': erdos_sim, 'Barabasi-Albert': barabasi_sim, 'Random scale-free': rsf_sim}

sim_dict2 = {'Regular': regular_sim, 'Erdos-Renyi': erdos_sim, 'REDS': reds_sim, 'Random scale-free': rsf_sim}

sim_dict3 = {'REDS': reds_sim, 'Small-world REDS': sw_reds_sim, 'RGG': rgg_sim}

mult_coop_by_b_plot(sim_dict1)
mult_coop_by_b_plot(sim_dict2)
mult_coop_by_b_plot(sim_dict3)



regular = gsd.load_sim_data('regular_params=1000-10-0_nets=5_sims=5.gsdata')
erdos = gsd.load_sim_data('erdos_renyi_params=1000-10-1_nets=5_sims=5.gsdata')
barabasi = gsd.load_sim_data('barabasi_albert_params=1000-5_nets=5_sims=5.gsdata')
r_scale_free = gsd.load_sim_data('random_scale_free_params=1000-5_nets=5_sims=5.gsdata')
reds = gsd.load_sim_data('reds_params=1000-0.1-0.146-1.0_nets=5_sims=5.gsdata')
sw_reds = gsd.load_sim_data('smallworld_reds_params=1000-0.1-0.146-1.0-0.2_nets=5_sims=5.gsdata')
rgg = gsd.load_sim_data('rgg_params=1000-10_nets=5_sims=5.gsdata')

reds_sim = gsd.load_sim_data('reds_params=1000-0.1-0.146-1.0_nets=5_sims=5.gsdata')
comm_reds_sim = gsd.load_sim_data('comm_reds_params=1000-0.1-0.146-1.0_nets=5_sims=5.gsdata')
rand_reds_sim = gsd.load_sim_data('rand_reds_params=1000-0.1-0.146-1.0-1.0_nets=5_sims=5.gsdata')
comm_rand_reds_sim = gsd.load_sim_data('comm_rand_reds_params=1000-0.1-0.146-1.0-1.0_nets=5_sims=5.gsdata')

sim_dict_redsold = {'REDS': reds, 'Erdos-Renyi': erdos, 'Barabasi-Albert': barabasi, 'Regular': regular}

sim_dict = {'Standard': reds_sim, 'Random': rand_reds_sim, 'Community-Random': comm_rand_reds_sim, 'Community': comm_reds_sim}

def reds_e_range(n, r, s, num, max_e, min_e=0, depth=1) :
  step = (max_e-min_e)/float(num)
  e_list = np.arange(min_e, max_e+step, step)
  return {str(e):[reds_graph(n, r, e, s) for x in range(depth)] for e in e_list}
  
def connected_hist(reds_range) :
  my_dpi=300
  connected = {k: map(nx.is_connected, v) for k, v in reds_range.iteritems}
  keys = [float(k) for k, v in connected.iteritems()]
  rate_connected = [sum(v)/float(len(v)) for k, v in connected.iteritems()]
  rate_disconnected = [(len(v)-sum(v))/float(len(v)) for k, v in connected.iteritems()]
  fig = plt.figure(figsize=(6, 2), dpi = my_dpi)
  plt.bar(keys, rate_disconnected, bottom = rate_connected, color = '#adadad', label='Disconnected')
  plt.bar(keys, rate_connected, color = '#494949', label='Connected')
  plt.legend()
  plt.tick_params(labelsize=9)
  plt.ylabel('Rate of Connectivity', fontsize=10, weight='bold')
  plt.xlabel('E', fontsize=10, weight='bold', fontstyle='italic')
  plt.tight_layout()
  plt.savefig(data_directory+'connect_hist.png', dpi=my_dpi)
  
    
  
def plot_path_lengths(e_range) :
  lengths = [e.graph['char_path_length'] for e in e_range]
  energies = [e.graph['energy'] for e in e_range]
  my_dpi = 300
  fig = plt.figure(figsize=(6, 4), dpi = my_dpi)
  plt.plot(energies, lengths, 'r-', linewidth=6.0)
  plt.xlabel('Energy', fontsize=17, style='italic', weight='bold')
  plt.ylabel('Char. Path Length', fontsize=17, weight='bold')
  plt.tight_layout()
  plt.savefig(data_directory+'char_paths_narrow.png', dpi = my_dpi)

def plot_connected(e_range) :
  energies = [e.graph['energy'] for e in e_range]
  connected = []
  disconnected = []
  for i in range(len(e_range)) :
    if e_range[i].graph['char_path_length']>0 :
      connected.append(energies[i])
    else :
      disconnected.append(energies[i])
  my_dpi = 300
  m_size = 10
  fig = plt.figure(figsize=(6, 1.75), dpi = my_dpi)
  ax = plt.axes(frameon=False)
  ax.axes.get_yaxis().set_visible(False)
  plt.plot(connected, np.zeros_like(connected), 'bx', label='Connected', markersize=m_size)
  plt.plot(disconnected, np.zeros_like(disconnected), 'ro', label='Disconnected', markersize=m_size)
  plt.xlabel('Energy', fontsize=17, style='italic', weight='bold')
  plt.yticks([])
  plt.ylim(-0.05, 0.2)
  xmin = min(energies)
  xmax = max(energies)
  ymin, ymax = ax.get_yaxis().get_view_interval()
  ax.add_artist(Line2D((xmin, xmax), (ymin, ymin), color='black', linewidth=2))
  plt.legend()
  plt.tight_layout()
  plt.savefig(data_directory+'is_connected_narrow.png', dpi = my_dpi)
  
def svm(e_range, l=0, steps=80) :
  energies = [e.graph['energy'] for e in e_range]
  e_max = max(energies)
  e_min = min(energies)
  s = 10/float(e_max-e_min)
  step = (e_max-e_min)/steps
  D = [{'y' : 1 if e.graph['char_path_length']>0 else -1, 'e': e.graph['energy']} for e in e_range]
  W = np.arange(e_min, e_max+step, step)
  loss = [svm_loss(D, w, s, l) for w in W]
  return {'w' : W, 'loss' : loss}
  
def score(d, w, s) :
  return s*d['y']*(d['e']-w)

def svm_loss(D, w, s, l) :
  hinges = [max(0, 1-score(d, w, s)) for d in D]
  return (sum(hinges)/len(hinges)+l*s)

def mult_coop_by_b_plot_poster(sim_dict) :
  n = len(sim_dict)
  my_dpi=96
  fig = plt.figure(figsize=(10.1, 8.44), dpi=my_dpi)
  ax = fig.add_subplot('111')
  ax.set_prop_cycle(cycler('color', ['c', 'm', 'y', 'k']) + cycler('linestyle', ['-', '--', '-.', ':']))
  filename = 'coop_by_b'
  for name, sim in sim_dict.iteritems() :
    filename = filename + '_' + name
    gsa.cooperation_by_b_plot(sim, name)
  #plt.title('Co-operation Ratios for Random Graphs', fontsize=40)
  ax.tick_params(labelsize=14)
  plt.xlabel('Temptation to Defect', fontsize=17, weight='bold')
  plt.legend(loc=(0.7, 0.82), prop={'size': 16})
  plt.tight_layout()
  plt.savefig(data_directory+'POSTER_'+filename+'_k=10_small.png', dpi=my_dpi)

  

dict = {'barabasi-albert': [nx.barabasi_albert_graph(1000, 5) for x in range(10)], 'erdos-renyi': [nx.watts_strogatz_graph(1000, 10, 1) for x in range(10)], 'reds': [reds_graph(1000, 0.1, 0.146, 1.0) for x in range(10)]}
for k, v in dict.iteritems() :
  map(social_properties, v)

  
net_dict = {}
  
for k, s in sim_dict.iteritems() :
  net_dict[k] = []
  for m in s['networks'] :
    social_properties(m['network'])
    net_dict[k].append(m['network'])
  